#!/bin/bash

set -e  # Salir inmediatamente si un comando falla

# Configuración de colores para mensajes
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
RED="\033[0;31m"
NC="\033[0m" # Sin color

log() {
    echo -e "${GREEN}==>${NC} $1"
}

warn() {
    echo -e "${YELLOW}==>${NC} $1"
}

error() {
    echo -e "${RED}==>${NC} $1"
}

# Paso 1: Detener servicios en el servidor
stop_server_services() {
    log "Deteniendo servicios en el servidor..."
    sudo systemctl stop ank-agent.service
    sudo systemctl stop ank-server.service
    log "Servicios en el servidor detenidos."
}

# Paso 2: Detener servicios y contenedores en el agente remoto
stop_agent_services() {
    log "Deteniendo servicios en el agente remoto..."

    # Pedir usuario SSH e IP del agente
    read -p "Introduce el usuario SSH del agente (ej. natxozm13): " SSH_USER
    read -p "Introduce la IP del agente (ej. 192.168.1.10): " AGENT_IP

    # Comando remoto para detener contenedores relacionados
    REMOTE_COMMAND="
         podman rm -a;
         podman rma -a;
    "
    #    podman ps -a | grep speed-consumer | awk '{print \$1}' | xargs -r podman stop;
    #    podman ps -a | grep speed-consumer | awk '{print \$1}' | xargs -r podman rm;
    #"

    ssh "$SSH_USER@$AGENT_IP" "$REMOTE_COMMAND"

    if [ $? -eq 0 ]; then
        log "Servicios y contenedores en el agente remoto detenidos."
    else
        error "Error al detener servicios en el agente remoto $AGENT_IP."
    fi
}

# Paso 3: Detener contenedores relacionados en el servidor
stop_server_containers() {
    log "Deteniendo contenedores en el servidor..."
    #sudo podman ps -a | grep mqtt-broker | awk '{print $1}' | xargs -r sudo podman stop
    #sudo podman ps -a | grep mqtt-broker | awk '{print $1}' | xargs -r sudo podman rm

    #sudo podman ps -a | grep speed-provider | awk '{print $1}' | xargs -r sudo podman stop
    #sudo podman ps -a | grep speed-provider | awk '{print $1}' | xargs -r sudo podman rm

    sudo podman rm -a
    sudo podman rmi -a

    log "Contenedores en el servidor detenidos y eliminados."
}

# Ejecución del script
main() {
    log "Automatización de cierre de Eclipse Ankaios."
    stop_server_services
    stop_agent_services
    stop_server_containers
    log "Cierre completado."
}

main
