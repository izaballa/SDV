import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped
import serial
from pyvesc import VESC

class VESCNode(Node):
    def __init__(self):
        super().__init__('vesc_node')

        # Parámetros
        self.vesc_port = self.declare_parameter('vesc_port', '/dev/ttyACM0').get_parameter_value().string_value
        self.vesc_baudrate = self.declare_parameter('vesc_baudrate', 115200).get_parameter_value().integer_value
        
        # Inicializa la conexión con el VESC
        try:
            self.serial = serial.Serial(self.vesc_port, self.vesc_baudrate)
            self.get_logger().info(f"Connected to VESC on {self.vesc_port}")
        except serial.SerialException as e:
            self.get_logger().error(f"Error connecting to VESC: {e}")
            return

        # Suscriptor al tópico /drive
        self.subscription = self.create_subscription(
            AckermannDriveStamped,
            '/drive',
            self.drive_callback,
            10
        )

    def drive_callback(self, msg):
        try:
            # Extraer velocidad y dirección
            speed = msg.drive.speed
            steering_angle = msg.drive.steering_angle

            # Comando de velocidad (ejemplo usando duty cycle)
            duty_cycle = speed / 10.0  # Ajusta según las necesidades de tu coche
            self.serial.write(VESC.SetDutyCycle(duty_cycle))

            self.get_logger().info(f"Sent speed: {speed}, steering_angle: {steering_angle}")
        except Exception as e:
            self.get_logger().error(f"Error sending command to VESC: {e}")

    def destroy_node(self):
        self.serial.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = VESCNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down VESC node.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
