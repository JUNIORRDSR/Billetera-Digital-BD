CREATE TABLE `Clientes`(
    `id_cliente` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(255) NOT NULL,
    `apellido` VARCHAR(255) NOT NULL,
    `documento_identidad` INT(10) NOT NULL,
    `correo_electronico` VARCHAR(100) NOT NULL,
    `fecha_nacimiento` DATE NOT NULL,
    `fecha_registro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP());
CREATE TABLE `Cuentas`(
    `id_cuenta` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_cliente` INT NOT NULL,
    `saldo_actual` DECIMAL(10, 2) NOT NULL,
    `tipo_cuenta` ENUM('"corriente"', '"cats"', '"ahorro"') NOT NULL,
    `fecha_apertura` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(), `clave_ingreso` INT(4) NOT NULL, `numero_telefono_ingreso` INT(11) NOT NULL);
ALTER TABLE
    `Cuentas` ADD UNIQUE `cuentas_id_cliente_unique`(`id_cliente`);
CREATE TABLE `Deposito`(
    `id_deposito` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_cuenta` INT NOT NULL,
    `monto` DECIMAL(8, 2) NOT NULL,
    `fecha_deposito` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(), `canal` VARCHAR(50) NOT NULL, `estado` ENUM(
        '"completado"',
        '"en proceso"',
        '"rechazado"'
    ) NOT NULL);
ALTER TABLE
    `Deposito` ADD INDEX `deposito_id_cuenta_index`(`id_cuenta`);
CREATE TABLE `Retiros`(
    `id_retiro` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_cuenta` INT NOT NULL,
    `monto` DECIMAL(10, 2) NOT NULL,
    `fecha_retiro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(), `canal_retiro` VARCHAR(50) NOT NULL, `codigo_retiro` VARCHAR(50) NOT NULL, `estado` ENUM(
        '"completado"',
        '"en proceso"',
        '"rechazado"'
    ) NOT NULL);
ALTER TABLE
    `Retiros` ADD INDEX `retiros_id_cuenta_index`(`id_cuenta`);
CREATE TABLE `Servicios`(
    `id_servicio` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre_servicio` VARCHAR(255) NOT NULL,
    `categoria` ENUM(
        '"Agua"',
        '"Luz"',
        '"Gas"',
        '"Servicio móvil"'
    ) NOT NULL,
    `descripcion` TEXT NOT NULL
);
CREATE TABLE `PagosServicios`(
    `id_pago` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_cuenta` INT NOT NULL,
    `id_servicio` INT NOT NULL,
    `monto` DECIMAL(10, 2) NOT NULL,
    `fecha_pago` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(), `estado` ENUM(
        '"completado"',
        '"en proceso"',
        '"rechazado"'
    ) NOT NULL);
ALTER TABLE
    `PagosServicios` ADD INDEX `pagosservicios_id_cuenta_index`(`id_cuenta`);
ALTER TABLE
    `PagosServicios` ADD INDEX `pagosservicios_id_servicio_index`(`id_servicio`);
CREATE TABLE `Transaccion`(
    `id_transaccion` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_cuenta_origen` INT NOT NULL,
    `id_cuenta_envio` INT NOT NULL,
    `monto` DECIMAL(10, 2) NOT NULL,
    `fecha_transaccion` TIMESTAMP NOT NULL,
    `canal` VARCHAR(255) NOT NULL,
    `estado` ENUM(
        '"completado"',
        '"en proceso"',
        '"rechazado"'
    ) NOT NULL
);
ALTER TABLE
    `Transaccion` ADD INDEX `transaccion_id_cuenta_origen_index`(`id_cuenta_origen`);
ALTER TABLE
    `Transaccion` ADD INDEX `transaccion_id_cuenta_envio_index`(`id_cuenta_envio`);
ALTER TABLE
    `PagosServicios` ADD CONSTRAINT `pagosservicios_id_servicio_foreign` FOREIGN KEY(`id_servicio`) REFERENCES `Servicios`(`id_servicio`);
ALTER TABLE
    `Retiros` ADD CONSTRAINT `retiros_id_cuenta_foreign` FOREIGN KEY(`id_cuenta`) REFERENCES `Cuentas`(`id_cuenta`);
ALTER TABLE
    `Cuentas` ADD CONSTRAINT `cuentas_id_cliente_foreign` FOREIGN KEY(`id_cliente`) REFERENCES `Clientes`(`id_cliente`);
ALTER TABLE
    `PagosServicios` ADD CONSTRAINT `pagosservicios_id_cuenta_foreign` FOREIGN KEY(`id_cuenta`) REFERENCES `Cuentas`(`id_cuenta`);
ALTER TABLE
    `Transaccion` ADD CONSTRAINT `transaccion_id_cuenta_origen_foreign` FOREIGN KEY(`id_cuenta_origen`) REFERENCES `Cuentas`(`id_cuenta`);
ALTER TABLE
    `Deposito` ADD CONSTRAINT `deposito_id_cuenta_foreign` FOREIGN KEY(`id_cuenta`) REFERENCES `Cuentas`(`id_cuenta`);
ALTER TABLE
    `Transaccion` ADD CONSTRAINT `transaccion_id_cuenta_envio_foreign` FOREIGN KEY(`id_cuenta_envio`) REFERENCES `Cuentas`(`id_cuenta`);