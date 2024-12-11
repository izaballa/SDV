function updateSpeed() {
    fetch('/speed')
        .then(response => response.json())
        .then(data => {
            document.getElementById('speed-value').textContent = data.speed;
        })
        .catch(error => console.error('Error fetching speed:', error));
}

// Actualiza cada segundo
setInterval(updateSpeed, 1000);
