# Usa una imagen base de ROS2 (Foxy)
FROM docker.io/library/ros:foxy

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-foxy-ackermann-msgs \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /ros2_ws/requirements.txt

# Instalar dependencias de Python desde requirements.txt
RUN pip3 install -r /ros2_ws/requirements.txt

# Instalar la librería paho-mqtt
RUN pip3 install paho-mqtt

# Configurar las variables de entorno para ROS2
ENV ROS_DOMAIN_ID=0
ENV ROS_IP=192.168.1.12
ENV ROS_HOSTNAME=192.168.1.12
ENV ROS_DISTRO=foxy

# Fuente del bashrc para garantizar que las variables estén disponibles
RUN /bin/bash -c "source ~/.bashrc"

# Crear espacio de trabajo ROS2
WORKDIR /ros2_ws

# Copiar el paquete y otros archivos al espacio de trabajo
COPY ../mqtt_ros2 /ros2_ws/mqtt_ros2

# Establecer el directorio de trabajo
WORKDIR /ros2_ws/mqtt_ros2

# Configurar, compilar el paquete y comando de entrada para lanzar el nodo
CMD ["/bin/bash", "-c", "colcon build && source install/setup.bash && ros2 launch mqtt_ros2 speed_provider.launch.py"]