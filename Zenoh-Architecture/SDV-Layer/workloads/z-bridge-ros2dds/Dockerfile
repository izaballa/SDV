# Uses the base image of the Eclipse Zenoh Bridge
FROM docker.io/eclipse/zenoh-bridge-ros2dds:latest

# Copy the configuration file from your machine to the container
COPY bridge-config.json5 /bridge-config.json5

# Default command to run the container
CMD ["-c", "/bridge-config.json5"]
