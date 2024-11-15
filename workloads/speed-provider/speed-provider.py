import os
import time
import sys
from datetime import datetime
import paho.mqtt.client as mqtt
from flask import Flask, request, render_template

# Configuración de conexión MQTT
mqtt_broker = os.environ.get('MQTT_BROKER_ADDR', '127.0.0.1')
mqtt_port = int(os.environ.get('MQTT_BROKER_PORT', '1883'))
mode = os.environ.get('SPEED_PROVIDER_MODE', 'webui')

app = Flask(__name__, template_folder='templates')

# Inicializar el cliente MQTT
client = mqtt.Client()

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now} {msg}", file=sys.stderr, flush=True)

# Conectar al broker MQTT
def connect_mqtt():
    client.reconnect_delay_set(min_delay=1, max_delay=120)  # Configuración de reconexión
    client.connect(mqtt_broker, mqtt_port, 60)
    client.loop_start()

# Publicar la velocidad en el topic MQTT con QoS y confirmación de publicación
def publish_speed(speed):
    topic = "Vehicle/Speed"
    msg_info = client.publish(topic, speed, qos=1)  # QoS=1 para entrega garantizada al menos una vez
    msg_info.wait_for_publish()  # Esperar a que el mensaje se publique correctamente
    log(f"Feeding Vehicle.Speed to {speed}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'vehiclespeed' in request.form:
            speed = float(request.form['vehiclespeed'])
            publish_speed(speed)
            result = "Vehicle.Speed of {} km/h has been sent.".format(speed)
            return render_template('index.html', result=result)
    return render_template('index.html')

def automatic():
    while True:
        for speed in range(0, 100):
            publish_speed(speed)
            time.sleep(1)
        for speed in range(100, 0, -1):
            publish_speed(speed)
            time.sleep(1)

# Desconectar del broker MQTT de forma ordenada
def disconnect_mqtt():
    client.loop_stop()  # Detener el bucle del cliente MQTT
    client.disconnect()  # Desconectar del broker MQTT

if __name__ == '__main__':
    connect_mqtt()
    if mode == 'webui':
        log("Web UI mode")
        app.run(host='0.0.0.0', port=5000)
    elif mode == 'auto':
        log("Automatic mode")
        auto_thread = threading.Thread(target=automatic)
        auto_thread.start()
        auto_thread.join()
    finally:
        disconnect_mqtt()  # Asegurarse de que el cliente MQTT se desconecta correctamente
