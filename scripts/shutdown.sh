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

# Paso 1: Eliminar workloads
delete_workloads() {
    log "Eliminando workloads..."
    ank -k delete workload speed-consumer
    ank -k delete workload speed-provider
    ank -k delete workload mqtt-broker
}

# Paso 2: Detener servicios y contenedores en el agente remoto
stop_agent_services() {
    log "Deteniendo servicios en el agente remoto..."

    # Pedir usuario SSH e IP del agente
    read -p "Introduce el usuario SSH del agente (ej. natxozm13): " SSH_USER
    read -p "Introduce la IP del agente (ej. 192.168.1.10): " AGENT_IP

    ssh -t "$SSH_USER@$AGENT_IP" 'sudo systemctl stop ank-agent.service'

    if [ $? -eq 0 ]; then
        log "Servicios y contenedores en el agente remoto detenidos."
    else
        error "Error al detener servicios en el agente remoto $AGENT_IP."
    fi
}

# Paso 3: Detener servicios en el servidor
stop_server_services() {
    log "Deteniendo servicios en el servidor..."
    sudo systemctl stop ank-agent.service
    sudo systemctl stop ank-server.service
    log "Servicios en el servidor detenidos."
}

# Paso 4: Cerrar terminales
close_opened_terminals() {
    log "Cerrando terminales abiertas por gnome-terminal..."

    # Buscar y terminar procesos de terminal abiertos
    pkill gnome-terminal
    
    if [ $? -eq 0 ]; then
        log "Terminales cerradas correctamente."
    else
        warn "No se encontraron terminales abiertas para cerrar."
    fi
}


# Ejecución del script
main() {
    log "Automatización de cierre de Eclipse Ankaios."
    delete_workloads
    stop_agent_services
    stop_server_services
    close_opened_terminals
    log "Cierre completado."
}

main
