from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Ruta al archivo de configuración YAML
    config_file = os.path.join(
        get_package_share_directory('vesc'),  # Nombre del paquete
        'config',                             # Carpeta donde está el YAML
        'vesc_config.yaml'                    # Archivo de configuración
    )

    # Nodo VESC
    vesc_node = Node(
        package='vesc',                      # Nombre del paquete
        executable='vesc_node',              # Nodo a ejecutar
        name='vesc_node',                    # Nombre del nodo
        output='screen',                     # Mostrar salida en la terminal
        parameters=[config_file]             # Cargar parámetros del YAML
    )

    return LaunchDescription([
        vesc_node
    ])
