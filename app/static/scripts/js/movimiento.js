// Datos de ejemplo para simular movimientos
const movimientosSimulados = [
    {
        fecha: '2024-11-24 17:00:00',
        usuario: 'Camila Fernandez',
        cuenta: '1010-0010',
        tipo: 'Consignación',
        monto: 60000.00,
        referencia: 'REF010'
    },
    {
        fecha: '2024-11-24 16:00:00',
        usuario: 'Miguel Ramirez',
        cuenta: '1009-0009',
        tipo: 'Pago',
        monto: 70000.00,
        referencia: 'REF009'
    },
    {
        fecha: '2024-11-24 15:00:00',
        usuario: 'Sofia Diaz',
        cuenta: '1008-0008',
        tipo: 'Retiro',
        monto: 40000.00,
        referencia: 'REF008'
    },
    {
        fecha: '2024-11-24 14:00:00',
        usuario: 'Andres Torres',
        cuenta: '1007-0007',
        tipo: 'Consignación',
        monto: 40000.00,
        referencia: 'REF007'
    },
    {
        fecha: '2024-11-24 13:00:00',
        usuario: 'Laura Rodriguez',
        cuenta: '1006-0006',
        tipo: 'Pago',
        monto: 80000.00,
        referencia: 'REF006'
    },
    {
        fecha: '2024-11-24 12:00:00',
        usuario: 'Luis Garcia',
        cuenta: '1005-0005',
        tipo: 'Retiro',
        monto: 300000.00,
        referencia: 'REF005'
    },
    {
        fecha: '2024-11-24 11:00:00',
        usuario: 'Ana Lopez',
        cuenta: '1004-0004',
        tipo: 'Consignación',
        monto: 300000.00,
        referencia: 'REF004'
    },
    {
        fecha: '2024-11-24 10:00:00',
        usuario: 'Carlos Martinez',
        cuenta: '1003-0003',
        tipo: 'Pago',
        monto: 300000.00,
        referencia: 'REF003'
    },
    {
        fecha: '2024-11-24 09:00:00',
        usuario: 'Maria Gomez',
        cuenta: '1002-0002',
        tipo: 'Retiro',
        monto: 50000.00,
        referencia: 'REF002'
    },
    {
        fecha: '2024-11-24 08:00:00',
        usuario: 'Juan Perez',
        cuenta: '1001-0001',
        tipo: 'Consignación',
        monto: 100000.00,
        referencia: 'REF001'
    }
];

// Función para cargar los movimientos en la tabla
function cargarMovimientos(movimientos) {
    const tbody = document.getElementById('movimientos-body');
    tbody.innerHTML = ''; // Limpiar tabla

    movimientos.forEach(movimiento => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${movimiento.fecha}</td>
            <td>${movimiento.usuario}</td>
            <td>${movimiento.cuenta}</td>
            <td>${movimiento.tipo}</td>
            <td class="monto">${movimiento.monto.toFixed(2)}</td>
            <td>${movimiento.referencia}</td>
        `;
        tbody.appendChild(tr);
    });
}

// Función para obtener los movimientos desde la API
async function obtenerMovimientos() {
    try {
        const response = await fetch('/api/movimientos');
        if (!response.ok) {
            throw new Error('Error al obtener los movimientos');
        }
        const movimientos = await response.json();
        cargarMovimientos(movimientos);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Cargar movimientos cuando la página esté lista
document.addEventListener('DOMContentLoaded', obtenerMovimientos);

