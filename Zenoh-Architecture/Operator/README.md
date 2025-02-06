# Operations available on the operator

This document describes the operations that can be performed on the operator by using the Zenoh router REST API, controlling a ROS2 Turtlesim node and monitoring topics with a Zenoh subscriber.

## 1. Interacting with the Zenoh Router REST API

The following are the requests that can be made towards the Zenoh Router REST API:

### Deploy or update a workload
To deploy or update a workload, execute the following command:
```bash
curl -X PUT -H "Content-Type: application/yaml" --data-binary @<config_file>.yaml 'http://<IP-zenohd>:8000/vehicle/<ID_vehicle>/manifest/apply/req'
```

### Delete a workload
To delete a previously deployed workload, run:
```bash
curl -X PUT -H "Content-Type: application/yaml" --data-binary @<config_file>.yaml 'http://<IP_zenohd>:8000/vehicle/<ID_vehicle>/manifest/delete/req'
```

### Querying the current status of Eclipse Ankaios
To get the current status of Eclipse Ankaios, use:
```bash
curl -X PUT -d '["workloadStates"]' 'http://<IP_zenohd>:8000/vehicle/<ID-vehicle>/state/delete/req'
```

## 2. Remote control of a ROS2 node (Turtlesim)

You can control the movement of a ROS2 Turtlesim node (or any robot receiving Twist messages) with the following command:
```bash
python3 ros2_teleop.py -m client -e tcp/<IP_zenohd>:7447
```

## 3. Monitoring topics with a Zenoh subscriber

To deploy a Zenoh application that connects to the Zenoh router and subscribes to the topics specified in the -k option, run:
```bash
python3 z_sub.py -m client -e tcp/<IP_zenohd>:7447 -k 'vehicle/<ID_vehicle>/**'
```
