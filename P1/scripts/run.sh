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

# Paso 1: Configurar ank-server.service
configure_ank_server_service() {
    log "Editando el archivo /etc/systemd/system/ank-server.service"
    if grep -Fq -e '--address 0.0.0.0:25551' /etc/systemd/system/ank-server.service; then
        warn "La línea '--address 0.0.0.0:25551' ya está configurada."
    else
        sudo sed -i 's|ExecStart=/usr/local/bin/ank-server --insecure --startup-config /etc/ankaios/state.yaml|& --address 0.0.0.0:25551|' /etc/systemd/system/ank-server.service
        log "Línea '--address 0.0.0.0:25551' añadida."
    fi
}


# Paso 2: Cargar configuración inicial state.yaml
copy_state_yaml() {
    log "Copiando el archivo state.yaml desde la carpeta 'config'..."
    
    # Verificar si el archivo state.yaml existe en la carpeta config
    if [ -f "../config/state.yaml" ]; then
        sudo cp ../config/state.yaml /etc/ankaios/state.yaml 
        log "El archivo state.yaml ha sido copiado correctamente."
    else
        error "El archivo ../config/state.yaml no existe. Asegúrate de que está en la carpeta correcta."
        exit 1
    fi
}

# Paso 3: Iniciar ank-server y ank-agent en el servidor
start_server_services() {
    log "Iniciando ank-server y ank-agent en el servidor..."
    sudo systemctl start ank-server.service
    sudo systemctl start ank-agent.service
    log "Servicios iniciados."
}

# Paso 4: Iniciar ank-agent en el agente
start_agent1() {
    log "Iniciando ank-agent en el agente remoto (192.168.1.10)..."
    
    # IP del servidor Ankaios
    read -p "Introduce la IP del servidor Ankaios (ej. 192.168.1.11): " SERVER_IP

    # Pedir usuario SSH e IP del agente
    read -p "Introduce el usuario SSH del agente (ej. natxozm13): " SSH_USER
    read -p "Introduce la IP del agente (ej. 192.168.1.10): " AGENT_IP
    
    # Conectar por SSH y ejecutar el comando en la máquina remota 
    gnome-terminal -- bash -c "ssh \"$SSH_USER@$AGENT_IP\" 'ank-agent -k --name infotainment --server-url http://$SERVER_IP:25551'; exec bash"
    
    
    if [ $? -eq 0 ]; then
        log "Agente iniciado remotamente en $AGENT_IP."
    else
        error "Error al iniciar el agente en la máquina remota $AGENT_IP."
    fi
}

start_agent2() {
    log "Iniciando ank-agent en el agente remoto (192.168.1.12)..."
    
    # IP del servidor Ankaios
    read -p "Introduce la IP del servidor Ankaios (ej. 192.168.1.11): " SERVER_IP

    # Pedir usuario SSH e IP del agente
    read -p "Introduce el usuario SSH del agente (ej. natxozm13): " SSH_USER
    read -p "Introduce la IP del agente (ej. 192.168.1.12): " AGENT_IP
    
    # Conectar por SSH y ejecutar el comando en la máquina remota 
    gnome-terminal -- bash -c "ssh \"$SSH_USER@$AGENT_IP\" 'ank-agent -k --name agent_ros2 --server-url http://$SERVER_IP:25551'; exec bash"
    
    
    if [ $? -eq 0 ]; then
        log "Agente iniciado remotamente en $AGENT_IP."
    else
        error "Error al iniciar el agente en la máquina remota $AGENT_IP."
    fi
}

# Paso 5: Abrir ventanas de logs
show_logs() {
    log "Abriendo ventanas de logs..."
    
    log "Logs del servidor:"
    gnome-terminal -- bash -c "sudo journalctl -u ank-server -f; exec bash"
    gnome-terminal -- bash -c "sudo podman logs -f \$(sudo podman ps -a | grep mqtt-broker | awk '{print \$1}'); exec bash"
    gnome-terminal -- bash -c "sudo podman logs -f \$(sudo podman ps -a | grep speed-provider | awk '{print \$1}'); exec bash"
    
    #log "Logs del agente (remoto):" Ejecutar en terminal remota
    #gnome-terminal -- bash -c "ssh \"$SSH_USER@$AGENT_IP\" 'podman logs -f $(podman ps -a | grep speed-consumer | awk '{print $1}')'; exec bash"
    #podman logs -f $(podman ps -a | grep mqtt_ros2 | awk '{print $1}')
}

# Ejecución del script
main() {
    log "Automatización de puesta en marcha de Eclipse Ankaios."
    configure_ank_server_service
    copy_state_yaml
    start_server_services
    start_agent1
    start_agent2 
    show_logs
    log "Puesta en marcha completada."
}

main
