import os
import sys
from datetime import datetime
import paho.mqtt.client as mqtt

# Configuración de conexión MQTT
mqtt_broker = os.environ.get('MQTT_BROKER_ADDR', '127.0.0.1')
mqtt_port = int(os.environ.get('MQTT_BROKER_PORT', '1883'))
topic = "Vehicle/Speed"

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now} {msg}", file=sys.stderr, flush=True)

# Callback al conectar
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        log("Connected to MQTT broker")
        client.subscribe(topic)
        log(f"Subscribed to topic: {topic}")
    else:
        log(f"Failed to connect, return code: {rc}")

# Callback al recibir un mensaje
def on_message(client, userdata, message):
    try:
        speed = message.payload.decode()
        log(f"Received updated speed: {speed}")
    except Exception as e:
        log(f"Error decoding message: {e}")

# Callback para errores
def on_subscribe(client, userdata, mid, granted_qos):
    log(f"Subscription success, granted QoS: {granted_qos}")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        log("Unexpected disconnection. Reconnecting...")

# Configurar y conectar el cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect

client.reconnect_delay_set(min_delay=1, max_delay=120)  # Configurar reconexión automática
client.connect(mqtt_broker, mqtt_port, 60)
client.loop_start()

try:
    # Mantener el programa corriendo para recibir mensajes
    log("Waiting for messages. Press Ctrl+C to exit.")
    while True:
        pass
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    log("Stopping MQTT client")
finally:
    client.loop_stop()
    client.disconnect()
    log("MQTT client disconnected")
