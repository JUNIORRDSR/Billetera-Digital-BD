// Update balance on home page
function updateBalance() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    if (currentUser) {
        document.getElementById('total-balance').textContent = `$${currentUser.balance.toFixed(2)}`;
    }
}

// Run when the home page loads
updateBalance();

// Toggle sidebar en móvil
document.querySelector('.menu-toggle').addEventListener('click', function() {
    document.querySelector('.sidebar').classList.toggle('active');
});

// Actualizar nombre de usuario
function updateUserInfo() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    if (currentUser) {
        document.querySelector('.user-name').textContent = currentUser.fullName || 'Usuario';
    }
}

updateUserInfo();
updateBalance();

// Manejo del sidebar
const menuToggle = document.querySelector('.menu-toggle');
const sidebar = document.querySelector('.sidebar');
const overlay = document.querySelector('.overlay');
const closeButton = document.querySelector('.close-sidebar');

// Abrir sidebar
menuToggle.addEventListener('click', function() {
    sidebar.classList.add('active');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevenir scroll
});

// Cerrar sidebar (botón X)
closeButton.addEventListener('click', function() {
    sidebar.classList.remove('active');
    overlay.classList.remove('active');
    document.body.style.overflow = ''; // Restaurar scroll
});

// Cerrar sidebar (click en overlay)
overlay.addEventListener('click', function() {
    sidebar.classList.remove('active');
    overlay.classList.remove('active');
    document.body.style.overflow = ''; // Restaurar scroll
});

// Cerrar sidebar al seleccionar una opción
document.querySelectorAll('.menu a').forEach(link => {
    link.addEventListener('click', function() {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    });
});

