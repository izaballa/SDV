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
The Zenoh router is available as a Docker image. A single instance is deployed on the local host machine running:
```bash
podman run --init --net=host docker.io/eclipse/zenoh --rest-http-port 8000
```

The ports used by Zenoh are:
- **7447/tcp**: The Zenoh protocol via TCP.
- **8000/tcp**: The Zenoh REST API.

To support UDP multicast it is only supported on Linux using the ```--net=host``` option to make the container share the host's networking space. Although in this case it would not be needed, since Zenoh applications connect to the router with the locator as ```client``` with ````connect: {endpoints: [“tcp/<IP_zenohd>:7447”]}}````.

## Configuration options
A Zenoh configuration file can be provided via CLI to the Zenoh router.
- ```-c, --config <DEFAULT_CONFIG.json5>```: A JSON5 configuration file. [DEFAULT_CONFIG.json5](https://github.com/izaballa/SDV/blob/main/Zenoh-Architecture/Cloud-Layer/DEFAULT_CONFIG.json5) shows the schema of this file and the available options.
⚠️ This option is currently missing in Ubuntu 24.04 release.

## Zenoh router command line arguments
Zenoh router accepts the following arguments:
- ```-c, --config <PATH>```: The configuration file. Currently, this file must be a valid JSON5 or YAML file.
- ```-l, --listen <ENDPOINT>```: Locators on which this router will listen for incoming sessions. Repeat this option to open several listeners. The following endpoints are currently supported:
  - **TCP**: ```tcp/<host_name_or_IPv4_or_IPv6>:<port>```
  - **UDP**: ```udp/<host_name_or_IPv4_or_IPv6>:<port>```
  - **TCP+TLS**: ```tls/<host_name>:<port>```
  - **QUIC**: ```quic/<host_name>:<port>```
- ```-e, --connect <ENDPOINT>```: A peer locator this router will try to connect to. Repeat this option to connect to several peers or routers.
- ```-i, --id <ID>```: The identifier (as an hexadecimal string, with odd number of chars (e.g.: A0B23...) that ```zenohd``` must use. If not set, a random unsigned 128bit integer will be used. ⚠️ This identifier must be unique in the system and must be 16 bytes maximum (32 chars).
- ```-P, --plugin <PLUGIN>```: A plugin that must be loaded. You can give just the name of the plugin, ```zenohd``` will search for a library named ```libzenoh_plugin_\<name\>.so``` (exact name depending the OS). Or you can give such a string: ```"\<plugin_name\>:\<library_path\>"```. Repeat this option to load several plugins. If loading failed, ```zenohd``` will exit.
- ```--plugin-search-dir <PATH>```: Directory where to search for plugins libraries to load. Repeat this option to specify several search directories.
- ```--no-timestamp```: By default ```zenohd``` adds a HLC-generated Timestamp to each routed data if there isn't already one. This option disables this feature.
- ```--no-multicast-scouting```: By default ```zenohd``` replies to multicast scouting messages for being discovered by peers and clients. This option disables this feature.
- ```--rest-http-port <SOCKET>```: Configures HTTP interface for the REST API (enabled by default on port 8000). Accepted values:
  - A port number.
  - A string with format ```<local_ip>:<port_number>``` (to bind the HTTP server to a specific interface).
  - `none` to disable the REST API.
  - ```--cfg <CFG>```: Allows arbitrary configuration changes as column-separated ```KEY:VALUE``` pairs, where:
    - ```KEY``` must be a valid config path.
    - ```VALUE``` must be a valid JSON5 string that can be deserialized to the expected type for the ```KEY``` field.
- ```--adminspace-permissions <[r|w|rw|none]>```: Configure the read and/or write permissions on the admin space. Default is read only.
