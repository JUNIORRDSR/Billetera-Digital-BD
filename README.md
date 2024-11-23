# Billetera Digital

Desarrollar una Base de Datos Relacional que simule una billetera digital, similar a servicios como Nequi o Daviplata.

## Componentes del Proyecto

### Base de Datos Relacional
- Se usará una base de datos Relacional para el guardado y gestion de los datos.
- Incluye tablas para registrar la información de estos elementos.

### Diseño de Interfaces
- Utiliza Vercel para diseñar las interfaces que interactúan con la base de datos.
- Las interfaces permiten la gestión e interacción con los datos almacenados.

### Registro de Información
- Registra datos en las tablas correspondientes de la base de datos.
- Asegura que la información esté bien estructurada y sea accesible.

## Consideraciones para el Manejo de Transacciones

### Consignaciones
- Determinar cuándo, dónde, cómo y a qué cuenta se generan las consignaciones.
- Registrar la cuenta que realiza la consignación.

### Retiros
- Determinar cuándo, dónde y cómo se generan los retiros.
- Mantener el saldo actual de cada cuenta.
- Registrar los movimientos de cuentas en un determinado periodo de tiempo.

## Consideraciones para el Manejo de Servicios

### Compras
- Permitir la compra de paquetes y/o minutos de celular.

### Pagos
- Facilitar el pago de servicios públicos.
