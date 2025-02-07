# Router Zenoh

## How to install in Linux Debian
To install the latest release of the Zenoh router (```zenohd```) and its default plugins (REST API plugin and Storages Manager plugin) you can do as follows:

### Linux Debian
Add Eclipse Zenoh private repository to the sources list, and install the ```zenoh``` package:
```bash
echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" | sudo tee -a /etc/apt/sources.list.d/zenoh.list > /dev/null
sudo apt update
sudo apt install zenoh
````
Then you can start run ```zenohd```.

## Run Zenoh router in a Docker container 
El router Zenoh está disponible como imagen Docker. Se despliega una sola instancia en la máquina host local ejecutando:
```bash
podman run --init --net=host docker.io/eclipse/zenoh --rest-http-port 8000
```

Los puertos utilizados por Zenoh son:
- **7447/tcp**: El protocolo Zenoh via TCP.
- **8000/tcp**: La REST API Zenoh.

Para soportar UDP multicast solo se soporta en Linux utilizando la opción ```--net=host``` para hacer que el contenedor comparta el networking space del host. Aunque en este caso no se necesitaría, ya que las aplicaciones Zenoh se conectan al router con el locator como ```client``` con ```connect: {endpoints: ["tcp/<IP_zenohd>:7447"]}}```.

## Configuration options
A Zenoh configuration file can be provided via CLI to the Zenoh router.
- ```-c, --config <DEFAULT_CONFIG.json5>```: A JSON5 configuration file. [DEFAULT_CONFIG.json5](https://github.com/izaballa/SDV/blob/main/Zenoh-Architecture/Cloud-Layer/DEFAULT_CONFIG.json5) shows the schema of this file and the available options.
