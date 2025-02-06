Solicitudes a la REST API del router Zenoh (zenohd):
- curl -X PUT -H "Content-Type: application/yaml" --data-binary @<config_file>.yaml 'http://<IP-zenohd>:8000/vehicle/<ID_vehicle>/manifest/apply/req'
- curl -X PUT -H "Content-Type: application/yaml" --data-binary @<config_file>.yaml 'http://<IP-zenohd>:8000/vehicle/<ID_vehicle>/manifest/delete/req'
- curl -X PUT -d '["workloadStates"]' 'http://<IP_zenohd>:8000/vehicle/<ID-vehicle>/state/delete/req'

Teleoperador de un nodo ROS2 (Turtlesim):
- python3 ros2-teleop.py -m client -e tcp/<IP-zenohd>:7447

Monitorear topics desde el operador:
- xxx
