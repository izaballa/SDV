Implementation of an SDV architecture with Eclipse Ankaios + Zenoh

Para el despligue de esta prueba se utilizan tres máquinas virtuales (VM) que cada una simula:
- VM 1: Operador que realiza las operaciones de instalar/reconfigurar/eliminar un workload. Monitorizar valores publicados para las diferentes keys (topics) de la comunicación. Así como una prueba de teleoperador que controla un un nodo Turtlesim.
- VM 2: Cloud Layer que corre el router Zenoh que permite la comunicación entre el operador y los workloads que se corren en la VM 3.
- VM 3: El coche F1Tenth que corre Eclipse Ankaios, el orquestador de contenedores y workloads, y los nodos ROS2, aplicaciones robóticas.

Proof of concept (POC)

Para desplegar la prueba se empieza poniendo en marcha el router Zenoh con el comando:
podman run --init --net=host docker.io/eclipse/zenoh --rest-http-port 8000

Con la opción --rest-http-port 8000 se habilita en el router una REST API en el puerto 8000 para poder comunicar vía HTTP las máquinas VM 1 y VM 2.

Una vez desplegado el router Zenoh, se pasa ha activar Eclipse Ankaios en la VM 3 con los siguientes comandos:
sudo systemctl start ank-server.service
sudo systemctl start ank-agent.service

Antes de arrancar Ankaios hay que especificar en /etc/ankaios/state.yaml el despliegue de la aplicación básica encargada de gestionar la lógica de las solicitudes del operador: 
- z-fleet-connector: Contenedor que gestiona las solicitudes del operador para instalar/reconfigurar/eliminar un workload.

Con z-fleet-connector corriendo en la VM 3, ahora desde el operador se puede solicitan el despliegue de las dos aplicaciones básicas del funcionamiento de esta arquitectura:
- z-bridge-ros2dds
- 


![image](https://github.com/user-attachments/assets/df9d3872-9134-4821-bbfd-bd5fe37a3af8)
