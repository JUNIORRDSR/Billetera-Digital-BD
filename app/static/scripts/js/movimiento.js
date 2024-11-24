function loadTransactions() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const transactions = JSON.parse(localStorage.getItem('transactions')) || [];
    const userTransactions = transactions.filter(t => t.userId === currentUser.idNumber);

    const tbody = document.getElementById('movimientos-body');
    tbody.innerHTML = '';

    userTransactions.reverse().forEach(t => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${new Date(t.date).toLocaleString()}</td>
            <td>${currentUser.username}</td>
            <td>${t.accountNumber || 'Principal'}</td>
            <td>${t.type}</td>
            <td>${t.amount.toFixed(2)}</td>
            <td>${t.reference || '-'}</td>
        `;
        tbody.appendChild(row);
    });
}

// Load transactions when the page loads
loadTransactions();

