// ns.js

export function enviarMensaje() {
    var entradaUsuario = document.getElementById('entrada').value;
    document.getElementById('entrada').value = '';

    // Enviar la entrada del usuario al servidor
    fetch('/enviar_mensaje', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'entrada_usuario=' + encodeURIComponent(entradaUsuario),
    })
    .then(response => response.json())
    .then(data => {
        // Mostrar la respuesta del asistente en el chat
        document.getElementById('chat').innerHTML += '<p>Usuario: ' + entradaUsuario + '</p>';
        document.getElementById('chat').innerHTML += '<p>Asistente: ' + data.respuesta + '</p>';
    });
}
// Agregar un EventListener para el evento click del botón
document.querySelector('button').addEventListener('click', enviarMensaje);