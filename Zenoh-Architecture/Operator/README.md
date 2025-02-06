# Operaciones disponibles en el operador

Este documento describe las operaciones que se pueden realizar en el operador mediante el uso de la API REST del router Zenoh, el control de un nodo ROS2 Turtlesim y la monitorización de tópicos con un suscriptor Zenoh.

## 1. Interacción con la API REST de Zenoh Router

A continuación, se detallan las solicitudes que se pueden realizar hacia la API REST del router Zenoh:

### Desplegar o actualizar un workload
Para desplegar o actualizar un workload, ejecutar el siguiente comando:
```bash
curl -X PUT -H "Content-Type: application/yaml" --data-binary @<config_file>.yaml 'http://<IP-zenohd>:8000/vehicle/<ID_vehicle>/manifest/apply/req'
```

### Eliminar un workload
Para eliminar un workload previamente desplegado, ejecutar:
```bash
curl -X PUT -H "Content-Type: application/yaml" --data-binary @<config_file>.yaml 'http://<IP_zenohd>:8000/vehicle/<ID_vehicle>/manifest/delete/req'
```

### Consultar el estado actual de Eclipse Ankaios
Para obtener el estado actual de Eclipse Ankaios, usar:
```bash
curl -X PUT -d '["workloadStates"]' 'http://<IP_zenohd>:8000/vehicle/<ID-vehicle>/state/delete/req'
```

## 2. Control remoto de un nodo ROS2 (Turtlesim)

Se puede controlar el movimiento de un nodo ROS2 Turtlesim (o cualquier robot que reciba mensajes Twist) con el siguiente comando:
```bash
python3 ros2_teleop.py -m client -e tcp/<IP_zenohd>:7447
```

## 3. Monitorización de tópicos con un suscriptor Zenoh

Para desplegar una aplicación Zenoh que se conecte al router Zenoh y se suscriba a los tópicos especificados en la opción -k, ejecutar:
```bash
python3 z_sub.py -m client -e tcp/<IP_zenohd>:7447 -k 'vehicle/<ID_vehicle>/**'
```
