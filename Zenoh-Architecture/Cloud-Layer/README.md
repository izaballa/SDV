# Router Zenoh

El router Zenoh está disponible como imagen Docker. Se despliega una sola instancia en la máquina host local ejecutando:
```bash
podman run --init --net=host docker.io/eclipse/zenoh --rest-http-port 8000
```

Los puertos utilizados por Zenoh son:
- **7447/tcp**: El protocolo Zenoh via TCP.
- **8000/tcp**: La REST API Zenoh.

Para soportar UDP multicast solo se soporta en Linux utilizando la opción --net=host para hacer que el contenedor comparta el networking space del host. Aunque en este caso no se necesitaría, ya que las aplicaciones Zenoh se conectan al router con el locator como client con ```bash connect: {endpoints: ["tcp/<IP_zenohd>:7447"]}}```.

Router Zenoh (zenohd) en contenedor:
- podman run --init --net=host docker.io/eclipse/zenoh --rest-http-port 8000
Router Zenoh (zenohd) en binario:
- zenohd --rest-http-port 8000

Instalación en Ubuntu:
Add Eclipse Zenoh private repository to the sources list, and install the zenoh package:
echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" | sudo tee -a /etc/apt/sources.list.d/zenoh.list > /dev/null
sudo apt update
sudo apt install zenoh
Then you can start run zenohd.
