console.log('Script de inicio de sesión cargado'); // Mensaje para verificar que el script se carga
const form = document.getElementById('login-form');
if (form) {
    console.log('Formulario de inicio de sesión encontrado'); // Mensaje para verificar que el formulario se encuentra
    iniciarProcesoLogin(); // Iniciar el proceso de login
} else {
    console.error('Formulario de inicio de sesión no encontrado'); // Mensaje de error si no se encuentra el formulario
}

function iniciarProcesoLogin() {
    document.getElementById('iniciar-sesion').addEventListener('click', async function (event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto
        console.log('Formulario de inicio de sesión enviado'); // Mensaje de inicio

        // Obtener los valores de los campos del formulario
        const idType = document.getElementById('id-type').value; // Obtener el tipo de ID
        const idNumber = document.getElementById('id-number').value; // Obtener el número de ID
        const password = document.getElementById('password').value; // Obtener la contraseña

        console.log('Datos del formulario de inicio de sesión:', {
            idType,
            idNumber,
            password
        }); // Mensaje con los datos del formulario

        try {
            console.log('Enviando datos al servidor...'); // Mensaje antes de enviar
            const response = await fetch('/app/templates/pages/login.html', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json' // Cambiar a tipo de contenido JSON
                },
                body: JSON.stringify({
                    'id-type': idType,
                    'id-number': idNumber,
                    'password': password
                })
            });

            const result = await response.json(); // Obtener la respuesta JSON

            if (response.ok) {
                console.log('Inicio de sesión exitoso:', result.message); // Mensaje de éxito
                alert('Inicio de sesión exitoso.');
                window.location.href = '/app/templates/pages/inicio.html'; // Redirigir a la página de inicio
            } else {
                console.log('Error en el inicio de sesión:', result.error); // Mensaje de error
                alert('Error al iniciar sesión: ' + result.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Ocurrió un error al iniciar sesión. Inténtalo de nuevo más tarde.');
        }
    });
}


