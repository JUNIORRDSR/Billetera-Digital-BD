document.addEventListener('DOMContentLoaded', function() {
    // Obtener usuario y mostrar saldo
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const saldoDisplay = document.createElement('div');
    saldoDisplay.className = 'saldo-disponible';
    saldoDisplay.innerHTML = `<h3>Saldo disponible: $${currentUser.balance.toFixed(2)}</h3>`;
    document.getElementById('retiro-form').insertBefore(saldoDisplay, document.getElementById('retiro-form').firstChild);

    // Elementos del sidebar de código
    const codigoSidebar = document.getElementById('codigo-sidebar');
    const closeCodigo = document.querySelector('.close-codigo');
    const codigoBtn = document.querySelector('.codigo-btn');
    const form = document.getElementById('retiro-form');

    // Manejar envío del formulario
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const monto = parseFloat(document.getElementById('monto').value);
        
        // Validaciones
        if (isNaN(monto) || monto <= 0) {
            alert('Por favor, ingrese un monto válido.');
            return;
        }

        if (monto > currentUser.balance) {
            alert(`Saldo insuficiente. Su saldo disponible es: $${currentUser.balance.toFixed(2)}`);
            return;
        }

        // Recopilar datos
        const tipoRetiro = document.getElementById('tipo-retiro').value;
        const ciudad = document.getElementById('ciudad').value;
        const barrio = document.getElementById('barrio').value;
        const direccion = document.getElementById('direccion').value;

        // Generar código
        const codigo = Math.floor(100000 + Math.random() * 900000);

        // Actualizar saldo
        currentUser.balance -= monto;
        localStorage.setItem('currentUser', JSON.stringify(currentUser));

        // Registrar transacción
        addTransaction('Retiro', `Retiro con código ${codigo}`, -monto);

        // Actualizar sidebar
        document.querySelector('.codigo-display').textContent = codigo;
        document.getElementById('sidebar-monto').textContent = monto.toFixed(2);
        document.getElementById('sidebar-tipo-retiro').textContent = tipoRetiro;
        document.getElementById('sidebar-ciudad').textContent = ciudad;
        document.getElementById('sidebar-barrio').textContent = barrio;
        document.getElementById('sidebar-direccion').textContent = direccion;

        // Mostrar sidebar
        codigoSidebar.classList.add('active');

        // Actualizar saldo mostrado y limpiar formulario
        saldoDisplay.innerHTML = `<h3>Saldo disponible: $${currentUser.balance.toFixed(2)}</h3>`;
        this.reset();
    });

    // Cerrar sidebar
    const cerrarSidebar = () => {
        codigoSidebar.classList.remove('active');
    };

    closeCodigo.addEventListener('click', cerrarSidebar);
    codigoBtn.addEventListener('click', cerrarSidebar);
});

function addTransaction(type, description, amount) {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const transactions = JSON.parse(localStorage.getItem('transactions')) || [];
    
    transactions.push({
        userId: currentUser.idNumber,
        date: new Date().toISOString(),
        type,
        description,
        amount,
        balance: currentUser.balance
    });

    localStorage.setItem('transactions', JSON.stringify(transactions));
}


