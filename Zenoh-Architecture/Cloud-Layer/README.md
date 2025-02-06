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
