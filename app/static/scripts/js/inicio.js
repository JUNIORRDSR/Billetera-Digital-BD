document.addEventListener('DOMContentLoaded', async function() {
    try {
        // Realiza una solicitud para obtener el saldo al cargar la página
        const response = await fetch('/api/saldo');  // Cambia la ruta a la nueva API que devuelve el saldo
        if (!response.ok) {
            throw new Error('Error al obtener el saldo');
        }
        const data = await response.json();
        if (data.saldo !== undefined) {
            document.getElementById('total-balance').textContent = `$${data.saldo}`;
        } else {
            console.error(data.error);
        }
    } catch (error) {
        console.error('Error al obtener el saldo:', error);
    }
});