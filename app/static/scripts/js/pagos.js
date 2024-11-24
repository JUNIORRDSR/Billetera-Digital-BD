document.getElementById('pago-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const servicio = document.getElementById('servicio').value;
    const monto = parseFloat(document.getElementById('monto').value);
    const referencia = document.getElementById('referencia').value;

    if (isNaN(monto) || monto <= 0) {
        alert('Por favor, ingrese un monto válido.');
        return;
    }

    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    
    if (monto > currentUser.balance) {
        alert('Saldo insuficiente para realizar el pago.');
        return;
    }

    // Update user balance
    currentUser.balance -= monto;
    localStorage.setItem('currentUser', JSON.stringify(currentUser));

    // Add transaction to history
    addTransaction('Pago', `Pago de ${servicio} ${referencia ? '- Ref: ' + referencia : ''}`, -monto);

    alert('Pago realizado con éxito.');
    window.location.href = '/app/templates/index.html';
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

