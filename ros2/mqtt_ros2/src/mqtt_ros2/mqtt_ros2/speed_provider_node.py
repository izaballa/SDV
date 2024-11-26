import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped
import paho.mqtt.client as mqtt
import threading

class SpeedProviderNode(Node):
    def __init__(self):
        super().__init__('speed_provider_node')
        
        # Parámetros configurables (No pilla el *.yaml)
        self.mqtt_broker = self.declare_parameter('mqtt_broker', '192.168.1.11').get_parameter_value().string_value
        self.mqtt_port = self.declare_parameter('mqtt_port', 1883).get_parameter_value().integer_value
        self.mqtt_topic = self.declare_parameter('mqtt_topic', 'Vehicle/Speed').get_parameter_value().string_value
        self.ros_topic = self.declare_parameter('ros_topic', '/drive').get_parameter_value().string_value
        
        # Crear un publicador de ROS2
        self.publisher_ = self.create_publisher(AckermannDriveStamped, self.ros_topic, 10)
        
        # Inicializar cliente MQTT
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        
        # Conectar a MQTT en un hilo separado
        threading.Thread(target=self.connect_mqtt).start()

    def connect_mqtt(self):
        self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port, 60)
        self.mqtt_client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.get_logger().info(f"Connected to MQTT Broker at {self.mqtt_broker}:{self.mqtt_port}")
            self.mqtt_client.subscribe(self.mqtt_topic)
        else:
            self.get_logger().error(f"Failed to connect to MQTT Broker: {rc}")

    def on_message(self, client, userdata, msg):
        try:
            # Decodificar el mensaje recibido
            speed = float(msg.payload.decode())
            
            # Crear y publicar un mensaje AckermannDriveStamped
            ackermann_msg = AckermannDriveStamped()
            ackermann_msg.header.stamp = self.get_clock().now().to_msg()
            ackermann_msg.header.frame_id = 'base_link'  # Configurar el frame adecuado
            
            # Rellenar el campo de velocidad
            ackermann_msg.drive.speed = speed
            
            self.publisher_.publish(ackermann_msg)
            self.get_logger().info(f"Published speed: {speed} on {self.ros_topic}")
        except Exception as e:
            self.get_logger().error(f"Error processing MQTT message: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = SpeedProviderNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down node.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
