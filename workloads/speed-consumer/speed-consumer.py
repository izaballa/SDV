import os
import sys
import threading
from datetime import datetime
import time
import paho.mqtt.client as mqtt
from flask import Flask, render_template, jsonify

# Configuración de conexión MQTT
mqtt_broker = os.environ.get('MQTT_BROKER_ADDR', '127.0.0.1')
mqtt_port = int(os.environ.get('MQTT_BROKER_PORT', '1883'))

app = Flask(__name__, template_folder='templates')

# Variables globales
current_speed = "N/A"
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
    global current_speed
    try:
        current_speed = message.payload.decode()
        log(f"Received updated speed: {current_speed}")
    except Exception as e:
        log(f"Error decoding message: {e}")

# Conectar y configurar MQTT 
def connect_mqtt():
    try:
        client.reconnect_delay_set(min_delay=1, max_delay=120)
        client.connect(mqtt_broker, mqtt_port, 60)
        log("Connected to MQTT broker")
        client.loop_start()
    except Exception as e:
        log(f"Error connecting to MQTT broker: {e}")
        sys.exit(1)

# Desconectar MQTT
def disconnect_mqtt():
    client.loop_stop()
    client.disconnect()

# Rutas de Flask
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/speed')
def get_speed():
    return jsonify(speed=current_speed)

# Iniciar el servidor Flask
def start_webui():
    log("Starting Flask Web UI...")
    app.run(host='0.0.0.0', port=5000)

# Configuración del cliente MQTT
client = mqtt.Client()
# Registrar callbacks
client.on_connect = on_connect
client.on_message = on_message

if __name__ == '__main__':
    try:
        connect_mqtt()
        start_webui()
    except KeyboardInterrupt:
        log("Interrupt received, shutting down.")
    finally:
        disconnect_mqtt()
        log("MQTT client disconnected")
