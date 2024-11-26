console.log('Script de registro cargado'); // Mensaje para verificar que el script se carga
const form = document.getElementById('register-form');
if (form) {
    console.log('Formulario de registro encontrado'); // Mensaje para verificar que el formulario se encuentra
    console.log('Proceso de registro iniciado'); // Mensaje para verificar que el 
} else {
    console.error('Formulario de registro no encontrado'); // Mensaje de error si no se encuentra el formulario
}
function iniciarProcesoRegistro() {
    document.getElementById('crear-cuenta').addEventListener('click', async function (event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto
        console.log('Formulario enviado'); // Mensaje de inicio

        // Obtener los valores de los campos del formulario
        const firstName = document.getElementById('first-name').value; // Obtener el nombre
        const lastName = document.getElementById('last-name').value;   // Obtener el apellido
        const idType = document.getElementById('id-type').value;
        const idNumber = document.getElementById('id-number').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;
        const birthdate = document.getElementById('birthdate').value;
        const password = document.getElementById('password').value;

        console.log('Datos del formulario:', {
            firstName,
            lastName,
            idType,
            idNumber,
            phone,
            email,
            birthdate,
            password
        }); // Mensaje con los datos del formulario

        try {
            console.log('Enviando datos al servidor...'); // Mensaje antes de enviar
            const response = await fetch('/app/templates/pages/register.html', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json' // Cambiar a tipo de contenido JSON
                },
                body: JSON.stringify({
                    'id-type': idType,
                    'first-name': firstName,
                    'last-name': lastName,
                    'id-number': idNumber,
                    'phone': phone,
                    'email': email,
                    'birthdate': birthdate,
                    'password': password
                })
            });

            const result = await response.json(); // Obtener la respuesta JSON

            if (response.ok) {
                console.log('Registro exitoso:', result.message); // Mensaje de éxito
                alert('Verificación completa.');
                window.location.href = '/app/templates/pages/login.html'; // Redirigir a la página de inicio
            } else {
                console.log('Error en el registro:', result.error); // Mensaje de error
                alert('Error al registrar: ' + result.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Ocurrió un error al registrar. Inténtalo de nuevo más tarde.');
        }
    });
}

