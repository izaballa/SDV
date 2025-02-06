Implementation of an SDV architecture with Eclipse Ankaios + Zenoh

Para el despligue de esta prueba se utilizan tres máquinas virtuales (VM) que cada una simula:
- VM 1: Operador que realiza las operaciones de instalar/reconfigurar/eliminar un workload. Monitorizar valores publicados para las diferentes keys (topics) de la comunicación. Así como una prueba de teleoperador que controla un un nodo Turtlesim.
- VM 2: Cloud Layer que corre el router Zenoh que permite la comunicación entre el operador y los workloads que se corren en la VM 3.
- VM 3: El coche F1Tenth que corre Eclipse Ankaios, el orquestador de contenedores y workloads, y los nodos ROS2, aplicaciones robóticas.

Proof of concept (POC)

Para desplegar la prueba se empieza poniendo en marcha el router Zenoh con el comando:


![image](https://github.com/user-attachments/assets/df9d3872-9134-4821-bbfd-bd5fe37a3af8)
