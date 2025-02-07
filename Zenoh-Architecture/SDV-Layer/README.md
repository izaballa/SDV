# SDV Layer

## Eclipse Ankaios
[Eclipse Ankaios](https://github.com/eclipse-ankaios/ankaios/tree/main) provides workload and container orchestration for automotive High Performance Computing Software (HPCs). While it can be used for various fields of applications, it is developed from scratch for automotive use cases and provides a slim yet powerful solution to manage containerized applications. It supports container runtime Podman. Eclipse Ankaios is independent of existing communication frameworks like SOME/IP, DDS, or REST API.

Eclipse Ankaios manages multiple nodes and virtual machines with a single unique API in order to start, stop, configure, and update containers and workloads. It provides a central place to manage automotive applications with a setup consisting of one server and multiple agents. Usually one agent per node connects to one or more runtimes that are running the workloads.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6a9850b8-1ff9-492b-baaf-8d9d20d1998d" alt="image" width="800"/>
</p>

For more information, see the Eclipse Ankaios [documentation](https://eclipse-ankaios.github.io/ankaios/latest/).

### Installation
Ankaios has been tested with the following Linux distributions. Others might work as well but have not been tested.
- **Ubuntu 24.04 LTS**
- **Ubuntu 22.04 LTS**
- **Ubuntu 20.04 LTS**

#### System requirements
Ankaios currently requires a Linux OS and is available for ```x86_64``` and ```arm64``` targets.

The minimum system requirements are (tested with [EB corbos Linux – built on Ubuntu](https://www.elektrobit.com/products/ecu/eb-corbos/linux-built-on-ubuntu/)):

| Resource | Min      |
|----------|----------|
| CPU      | 1 core   |
| RAM      | 128 MB   |

[Podman](https://podman.io/) needs to be installed as this is used as container runtime. For using the ```podman``` runtime, Podman version 3.4.2 is sufficient but the ```podman-kube``` runtime requires at least Podman version 4.3.1.

The podman package is available in the official repositories for Ubuntu 20.10 and newer.
```bash
sudo apt-get update
sudo apt-get -y install podman
```

---
⚠️ On Ubuntu 24.04 there is a known problem with Podman stopping containers. The following workaround disables AppArmor for Podman. Run the following steps as root after installation of Podman:
```bash
mkdir -p /etc/containers/containers.conf.d
printf '[CONTAINERS]\napparmor_profile=""\n' > /etc/containers/containers.conf.d/disable-apparmor.conf
```
---

#### Setup with script
The recommended way to install Ankaios is using the installation script. To install the latest release version of Ankaios, please run the following command:
```bash
curl -sfL https://github.com/eclipse-ankaios/ankaios/releases/latest/download/install.sh | bash -
```
The installation process automatically detects the platform and downloads the appropriate binaries. The default installation path for the binaries is ```/usr/local/bin``` but can be changed. The installation also creates systemd unit files and an uninstall script.

## Utilidades SDV Layer

You can start workloads in Ankaios in a number of ways. For example, you can define a file with the startup configuration and use systemd to start Ankaios. The startup configuration file contains all of the workloads and their configuration that you want to be started by Ankaios. The default config is stored in ```/etc/ankaios/state.yaml```.

To start the Ankaios srever:
```bash
sudo systemctl start ank-server.service
```

The Ankaios server will read the config but detect that no agent is available that could start the workload. It is required start an agent:
```bash
sudo systemctl start ank-agent.service
```

This Ankaios agent will run the workload that has been assigned to it. We can use the Ankaios CLI to check the current state:
```bash
ank -k get state
```

Or use:

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
