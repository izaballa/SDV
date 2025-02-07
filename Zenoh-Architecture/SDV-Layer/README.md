SDV Layer





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
