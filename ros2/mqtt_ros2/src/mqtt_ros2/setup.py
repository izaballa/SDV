from setuptools import setup

package_name = 'mqtt_ros2'

setup(
    name=package_name,
    version='1.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/config', ['config/speed_provider_config.yaml']),
        ('share/' + package_name + '/launch', ['launch/speed_provider.launch.py']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='natxozm13',
    maintainer_email='izaballa@ikerlan.es',
    description='A ROS2 node for bridging MQTT and ROS2 topics',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'speed_provider_node = mqtt_ros2.speed_provider_node:main',
        ],
    },
)
