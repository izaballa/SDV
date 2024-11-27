from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mqtt_ros2',
            executable='speed_provider_node',
            name='speed_provider_node',
            output='screen',
            parameters=[
                '../config/speed_provider_config.yaml'
            ]
        ),
    ])
