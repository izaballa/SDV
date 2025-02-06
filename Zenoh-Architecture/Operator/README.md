Requests to the REST API of the Zenoh router (zenohd):
- curl -X PUT -H “Content-Type: application/yaml” --data-binary @<config_file>.yaml 'http://<IP-zenohd>:8000/vehicle/<ID_vehicle>/manifest/apply/req'
- curl -X PUT -H “Content-Type: application/yaml” --data-binary @<config_file>.yaml 'http://<IP-zenohd>:8000/vehicle/<ID_vehicle>/manifest/delete/req'
- curl -X PUT -d '[“workloadStates”]' 'http://<IP_zenohd>:8000/vehicle/<ID-vehicle>/state/delete/req'

Teleoperator of a ROS2 node (Turtlesim):
- python3 ros2_teleop.py -m client -e tcp/<IP_zenohd>:7447

Monitor topics from the operator with a Zenoh subscriber:
- python3 z_sub.py -m client -e tcp/<IP_zenohd>:7447 -k 'vehicle/<ID_vehicle>/**'
