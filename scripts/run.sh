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
#configure_ank_server_service() {
#    log "Editando el archivo /etc/systemd/system/ank-server.service"
#    if grep -Fq "--address 0.0.0.0:25551" /etc/systemd/system/ank-server.service; then
#        warn "La línea '--address 0.0.0.0:25551' ya está configurada."
#    else
#        sudo sed -i '/ExecStart=\/usr\/local\/bin\/ank-server --insecure --startup-config \/etc\/ankaios\/state.yaml/a --address 0.0.0.0:25551' /etc/systemd/system/ank-server.service
#        log "Línea '--address 0.0.0.0:25551' añadida."
#    fi
#}


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
start_agent() {
    log "Iniciando ank-agent en el agente remoto (192.168.1.10)..."
    
    # IP del servidor Ankaios
    read -p "Introduce la IP del servidor Ankaios (ej. 192.168.1.11): " SERVER_IP

    # Pedir usuario SSH e IP del agente
    read -p "Introduce el usuario SSH del agente (ej. natxozm13): " SSH_USER
    read -p "Introduce la IP del agente (ej. 192.168.1.10): " AGENT_IP

    # Comando remoto a ejecutar
    REMOTE_COMMAND="ank-agent -k --name infotainment --server-url http://$SERVER_IP:25551"
    
    # Conectar por SSH y ejecutar el comando en la máquina remota
    ssh "$SSH_USER@$AGENT_IP" "$REMOTE_COMMAND"
    
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
    
    log "Logs del agente (remoto):"
    ssh -t "$SSH_USER@$AGENT_IP" "podman logs -f \$(podman ps -a | grep speed-consumer | awk '{print \$1}')"
}

# Ejecución del script
main() {
    log "Automatización de puesta en marcha de Eclipse Ankaios."
    #configure_ank_server_service
    copy_state_yaml
    start_server_services
    start_agent
    show_logs
    log "Puesta en marcha completada."
}

main
