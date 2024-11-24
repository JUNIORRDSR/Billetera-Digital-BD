document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Detiene el envío normal del formulario
    
    // Obtener valores de los campos
    const fullName = document.getElementById('full-name').value;
    const idType = document.getElementById('id-type').value;
    const idNumber = document.getElementById('id-number').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
    const birthdate = document.getElementById('birthdate').value;
    const password = document.getElementById('password').value;

    // Verificar si algún campo está vacío
    if (!fullName || !idType || !idNumber || !phone || !email || !birthdate || !password) {
        alert('Por favor, complete todos los campos');
        return;
    }

    // Si todo está completo, redirigir
    window.location.href = '/app/templates/login.html';
});

