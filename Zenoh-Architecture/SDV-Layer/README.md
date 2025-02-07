# SDV Layer

## Eclipse Ankaios
[Eclipse Ankaios](https://github.com/eclipse-ankaios/ankaios/tree/main) provides workload and container orchestration for automotive High Performance Computing Software (HPCs). While it can be used for various fields of applications, it is developed from scratch for automotive use cases and provides a slim yet powerful solution to manage containerized applications. It supports container runtime Podman. Eclipse Ankaios is independent of existing communication frameworks like SOME/IP, DDS, or REST API.

Eclipse Ankaios manages multiple nodes and virtual machines with a single unique API in order to start, stop, configure, and update containers and workloads. It provides a central place to manage automotive applications with a setup consisting of one server and multiple agents. Usually one agent per node connects to one or more runtimes that are running the workloads.

![image](https://github.com/user-attachments/assets/6a9850b8-1ff9-492b-baaf-8d9d20d1998d) <img src="https://github.com/user-attachments/assets/6a9850b8-1ff9-492b-baaf-8d9d20d1998d" alt="image" width="1000"/>

For more information, see the Eclipse Ankaios [documentation](https://eclipse-ankaios.github.io/ankaios/latest/).



---
Comandos:
sudo nano /etc/ankaios/state.yaml

sudo systemctl start ank-server.service
sudo systemctl start ank-agent.service

watch ank -k get workloads
watch ank -k get agents

sudo journalctl -u ank.server -f
sudo journalctl -u ank.agent -f

ank -k apply <config_file>.yaml
ank -k delete workload <name_workload>

sudo podman images -a
sudo podman ps -a

sudo podman rm -a
sudo podman rmi -a

sudo systemctl stop ank-server.service
sudo systemctl stop ank-agent.service

sudo podman logs -f $(sudo podman ps -a | grep <name_workload> | awk '{print $1}')
