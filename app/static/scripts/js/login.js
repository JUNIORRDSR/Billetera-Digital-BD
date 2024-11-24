document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Validación básica que los campos no estén vacíos
    const idNumber = document.getElementById('id-number').value;
    const password = document.getElementById('password').value;

    if (!idNumber || !password) {
        alert('Por favor, complete todos los campos.');
        return;
    }

    // Redirigir directamente al index
    window.location.href = '/app/templates/index.html';
});


