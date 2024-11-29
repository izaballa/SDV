from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Ruta al archivo de configuración YAML
    config_file = os.path.join(
        get_package_share_directory('mqtt_ros2'),       # Nombre del paquete
        'config',                                       # Carpeta donde está el YAML
        'speed_provider_config.yaml'                    # Archivo de configuración
    )

    # Nodo VESC
    vesc_node = Node(
        package='mqtt_ros2',                           # Nombre del paquete
        executable='speed_provider_node',              # Nodo a ejecutar
        name='speed_provider_node',                    # Nombre del nodo
        output='screen',                               # Mostrar salida en la terminal
        parameters=[config_file]                       # Cargar parámetros del YAML
    )

    return LaunchDescription([
        vesc_node
    ])