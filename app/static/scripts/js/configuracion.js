document.addEventListener('DOMContentLoaded', function() {
    loadUserInfo();
    setupSidebar();
    // Obtener todos los botones de toggle password
    const toggleButtons = document.querySelectorAll('.toggle-password');
    
    // Agregar evento a cada botón
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Obtener el input asociado (hermano anterior)
            const input = this.parentElement.querySelector('input');
            
            // Cambiar el tipo de input
            if (input.type === 'password') {
                input.type = 'text';
                this.innerHTML = '<i class="fas fa-eye-slash"></i>';
            } else {
                input.type = 'password';
                this.innerHTML = '<i class="fas fa-eye"></i>';
            }
        });
    });
});

function loadUserInfo() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    if (currentUser) {
        // Información no editable
        document.getElementById('fullName').textContent = currentUser.fullName || '';
        document.getElementById('idType').textContent = currentUser.idType || '';
        document.getElementById('idNumber').textContent = currentUser.idNumber || '';
        document.getElementById('birthdate').textContent = currentUser.birthdate || '';
        
        // Información editable
        document.getElementById('emailDisplay').textContent = currentUser.email || '';
        document.getElementById('email').value = currentUser.email || '';
        document.getElementById('phoneDisplay').textContent = currentUser.phone || '';
        document.getElementById('phone').value = currentUser.phone || '';
    }
}

function updateEmail() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const newEmail = document.getElementById('email').value.trim();
    
    if (!newEmail) {
        alert('Por favor ingrese un correo válido');
        return;
    }
    
    currentUser.email = newEmail;
    localStorage.setItem('currentUser', JSON.stringify(currentUser));
    alert('Correo actualizado exitosamente');
}

function updatePhone() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const newPhone = document.getElementById('phone').value.trim();
    
    if (!newPhone) {
        alert('Por favor ingrese un teléfono válido');
        return;
    }
    
    currentUser.phone = newPhone;
    localStorage.setItem('currentUser', JSON.stringify(currentUser));
    alert('Teléfono actualizado exitosamente');
}

function updatePassword() {
    const currentPassword = document.getElementById('currentPassword').value;
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    
    if (!currentPassword || !newPassword || !confirmPassword) {
        alert('Por favor complete todos los campos');
        return;
    }
    
    if (newPassword !== confirmPassword) {
        alert('Las contraseñas no coinciden');
        return;
    }
    
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    if (currentPassword !== currentUser.password) {
        alert('La contraseña actual es incorrecta');
        return;
    }
    
    currentUser.password = newPassword;
    localStorage.setItem('currentUser', JSON.stringify(currentUser));
    alert('Contraseña actualizada exitosamente');
    
    // Limpiar campos
    document.getElementById('currentPassword').value = '';
    document.getElementById('newPassword').value = '';
    document.getElementById('confirmPassword').value = '';
}

// Manejo del sidebar (igual que en index.js)
function setupSidebar() {
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.overlay');
    const closeButton = document.querySelector('.close-sidebar');

    menuToggle.addEventListener('click', function() {
        sidebar.classList.add('active');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    });

    closeButton.addEventListener('click', function() {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    });

    overlay.addEventListener('click', function() {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    });
}

function toggleEdit(field) {
    const editForm = document.getElementById(`${field}Edit`);
    editForm.style.display = editForm.style.display === 'none' ? 'block' : 'none';
}

function cancelEdit(field) {
    const editForm = document.getElementById(`${field}Edit`);
    editForm.style.display = 'none';
    
    // Restaurar valores originales
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    if (field === 'email' || field === 'phone') {
        document.getElementById(field).value = currentUser[field] || '';
    } else if (field === 'password') {
        document.getElementById('currentPassword').value = '';
        document.getElementById('newPassword').value = '';
        document.getElementById('confirmPassword').value = '';
    }
}
