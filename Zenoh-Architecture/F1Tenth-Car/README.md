How to install it
To install the latest release of either the DDS plugin for the Zenoh router, either the zenoh-bridge-ros2dds standalone executable, you can do as follows:

Linux Debian
Add Eclipse Zenoh private repository to the sources list:
echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" | sudo tee -a /etc/apt/sources.list > /dev/null
sudo apt update
Then either:
- install the plugin with: sudo apt install zenoh-plugin-ros2dds.
- install the standalone executable with: sudo apt install zenoh-bridge-ros2dds.

Docker images
The zenoh-bridge-ros2dds standalone executable is also available as a Docker images for both amd64 and arm64. To get it, do:
- docker pull eclipse/zenoh-bridge-ros2dds:latest for the latest release
- docker pull eclipse/zenoh-bridge-ros2dds:nightly for the main branch version (nightly build)

Para poder utilizar zenoh-bridge-ros2dds en el coche F1Thenth hay que tener en cuenta que:
⚠️ The bridge relies on CycloneDDS and has been tested with RMW_IMPLEMENTATION=rmw_cyclonedds_cpp. While the DDS implementations are interoperable over UDP multicast and unicast, some specific and non-standard features of other DDS implementations (e.g. shared memory) might cause some issues.
It's important to make sure that NO DDS communication can occur between 2 hosts that are bridged by zenoh-bridge-ros2dds. Otherwise, some duplicate or looping traffic can occur.
To make sure of this, you can either:
- use ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST after Iron and ROS_LOCALHOST_ONLY=1 before Iron. Preferably, enable MULTICAST on the loopback interface with this command (on Linux): sudo ip l set lo multicast on
- use different ROS_DOMAIN_ID on each hosts
