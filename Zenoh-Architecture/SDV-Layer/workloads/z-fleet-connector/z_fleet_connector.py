from ankaios_sdk import Ankaios, Manifest
import zenoh
import json
import os
import logging
import sys
import threading

# Configuración del logger
logger = logging.getLogger("z-fleet-connector")
stdout = logging.StreamHandler(stream=sys.stdout)
stdout.setLevel(logging.INFO)
logger.addHandler(stdout)
logger.setLevel(logging.INFO)

# Inicialización del logging de Zenoh
zenoh.init_log_from_env_or("error")

# Configuración de Zenoh y Ankaios
ROUTER = os.getenv('ZENO_ROUTER_ADDR', 'tcp/192.168.1.11:7447')
VEHICLE_ID = os.getenv('VIN', 'default_vehicle')
BASE_TOPIC = f"vehicle/{VEHICLE_ID}"

# Evento para gestionar la ejecución del programa
shutdown_event = threading.Event()


def process_message(sample, ankaios, publishers):
    # Procesa los mensajes recibidos en los topics suscritos
    try:
        topic = sample.key_expr
        payload = sample.payload.to_string()
        logger.info(f"📩 Recibido: {topic} -> {payload}")

        if topic == f"{BASE_TOPIC}/manifest/apply/req":
            manifest = Manifest.from_string(payload)
            manifest.check()
            result = ankaios.apply_manifest(manifest)
            if result:
                publishers["apply_resp"].put(json.dumps(result.to_dict()))

        elif topic == f"{BASE_TOPIC}/manifest/delete/req":
            manifest = Manifest.from_string(payload)
            manifest.check()
            result = ankaios.delete_manifest(manifest)
            if result:
                publishers["delete_resp"].put(json.dumps(result.to_dict()))

        elif topic == f"{BASE_TOPIC}/state/req":
            state = ankaios.get_state(field_masks=json.loads(payload))
            publishers["state_resp"].put(json.dumps(state.to_dict()))

    except Exception as e:
        logger.error(f"❌ Error procesando mensaje: {e}", exc_info=True)


def main():
    # Función principal de la aplicación
    with Ankaios() as ankaios:
        conf = zenoh.Config()
        conf.insert_json5("mode", json.dumps("client"))
        conf.insert_json5("connect/endpoints", json.dumps([ROUTER]))

        with zenoh.open(conf) as session:
            # Declarar publicadores
            publishers = {
                "apply_resp": session.declare_publisher(f"{BASE_TOPIC}/manifest/apply/resp"),
                "delete_resp": session.declare_publisher(f"{BASE_TOPIC}/manifest/delete/resp"),
                "state_resp": session.declare_publisher(f"{BASE_TOPIC}/state/resp")
            }

            # Suscriptores
            session.declare_subscriber(
                f"{BASE_TOPIC}/manifest/apply/req",
                lambda sample: process_message(sample, ankaios, publishers)
            )
            session.declare_subscriber(
                f"{BASE_TOPIC}/manifest/delete/req",
                lambda sample: process_message(sample, ankaios, publishers)
            )
            session.declare_subscriber(
                f"{BASE_TOPIC}/state/req",
                lambda sample: process_message(sample, ankaios, publishers)
            )

            # Mantener la ejecución hasta que el contenedor sea detenido por Ankaios
            logger.info("🚀 Zenoh subscriber iniciado. Esperando mensajes...")
            shutdown_event.wait()  # Mantiene el proceso en ejecución 
            
            logger.info("🔻 Apagando Zenoh subscriber...")
            session.close()
            logger.info("✅ Sesión Zenoh cerrada.")

if __name__ == "__main__":
    main()
