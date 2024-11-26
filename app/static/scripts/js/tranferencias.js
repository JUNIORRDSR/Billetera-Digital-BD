console.log('Script de transferencias cargado'); // Mensaje para verificar que el script se carga
const form = document.getElementById('transferencia-form');
if (form) {
    console.log('Formulario de transferencia encontrado'); // Mensaje para verificar que el formulario se encuentra
    iniciarProcesoTransferencia(); // Iniciar el proceso de transferencia
} else {
    console.error('Formulario de transferencia no encontrado'); // Mensaje de error si no se encuentra el formulario
}

function iniciarProcesoTransferencia() {
    document.getElementById('transferencia-form').addEventListener('submit', async function (event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto
        console.log('Formulario de transferencia enviado'); // Mensaje de inicio

        // Obtener los valores de los campos del formulario
        const monto = parseFloat(document.getElementById('monto').value); // Obtener el monto
        const descripcion = document.getElementById('descripcion').value; // Obtener la descripción
        const cuentaDestino = document.getElementById('cuenta-destino').value; // Obtener la cuenta destino

        console.log('Datos del formulario de transferencia:', {
            monto,
            descripcion,
            cuentaDestino
        }); // Mensaje con los datos del formulario

        try {
            console.log('Enviando datos al servidor...'); // Mensaje antes de enviar
            const response = await fetch('/app/templates/pages/transferencias.html', { // Cambia esta ruta a la correcta
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json' // Cambiar a tipo de contenido JSON
                },
                body: JSON.stringify({
                    monto: monto,
                    descripcion: descripcion,
                    cuentaDestino: cuentaDestino
                })
            });

            const result = await response.json(); // Obtener la respuesta JSON

            if (response.ok) {
                console.log('Transferencia realizada con éxito:', result.message); // Mensaje de éxito
                alert('Transferencia realizada con éxito.');
                // Redirigir o actualizar la interfaz según sea necesario
                window.location.href = '/app/templates/pages/inicio.html'; // Redirigir a la página de inicio
            } else {
                console.log('Error al realizar la transferencia:', result.error); // Mensaje de error
                alert('Error al realizar la transferencia: ' + result.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Ocurrió un error al realizar la transferencia. Inténtalo de nuevo más tarde.');
        }
    });
}