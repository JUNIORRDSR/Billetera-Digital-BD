document.getElementById('transferencia-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const monto = parseFloat(document.getElementById('monto').value);
    const descripcion = document.getElementById('descripcion').value;
    const tipoConsignacion = document.getElementById('tipo-consignacion').value;
    const cuentaOrigen = document.getElementById('cuenta-origen').value;
    const cuentaDestino = document.getElementById('cuenta-destino').value;

    if (isNaN(monto) || monto <= 0) {
        alert('Por favor, ingrese un monto válido.');
        return;
    }

    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    
    if (monto > currentUser.balance) {
        alert('Saldo insuficiente para realizar la transferencia.');
        return;
    }

    // Update user balance
    currentUser.balance -= monto;
    localStorage.setItem('currentUser', JSON.stringify(currentUser));

    // Add transaction to history
    addTransaction('Transferencia', `${descripcion} - De: ${cuentaOrigen} A: ${cuentaDestino}`, -monto);

    alert('Transferencia realizada con éxito.');
    window.location.href = '../index.html';
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

