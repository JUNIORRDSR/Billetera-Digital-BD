-- MySQL Script generated by MySQL Workbench
-- Sun Nov 24 01:05:09 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema banco2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema banco2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `banco2` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `banco2` ;

-- -----------------------------------------------------
-- Table `banco2`.`consignacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco2`.`consignacion` (
  `id_consignacion` INT NOT NULL AUTO_INCREMENT,
  `telefono_origen` INT NOT NULL,
  `telefono_destino` INT NOT NULL,
  `monto` DECIMAL(15,2) NOT NULL,
  `descripcion` TEXT NULL,
  `procedencia` ENUM('Corresponsal Bancolombia', 'Nequi', 'otros Bancos') NOT NULL,
  PRIMARY KEY (`id_consignacion`),
  INDEX `consignacion_telefono_origen_index` (`telefono_origen` ASC) VISIBLE,
  INDEX `consignacion_telefono_destino_index` (`telefono_destino` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banco2`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco2`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `tipo_de_id` ENUM('cedula de ciudadania', 'cedula de extranjeria', 'pasaporte') NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `numero_documento` BIGINT NOT NULL,
  `telefono` VARCHAR(255) NOT NULL,
  `correo` VARCHAR(255) NOT NULL,
  `fecha_nacimiento` DATE NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `usuario_numero_documento_unique` (`numero_documento` ASC) VISIBLE,
  UNIQUE INDEX `usuario_telefono_unique` (`telefono` ASC) VISIBLE,
  UNIQUE INDEX `usuario_correo_unique` (`correo` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banco2`.`cuenta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco2`.`cuenta` (
  `id_cuenta` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `numero_de_cuenta` VARCHAR(255) NOT NULL,
  `saldo` DECIMAL(15,2) NOT NULL,
  PRIMARY KEY (`id_cuenta`),
  UNIQUE INDEX `cuenta_id_usuario_unique` (`id_usuario` ASC) VISIBLE,
  UNIQUE INDEX `cuenta_numero_de_cuenta_unique` (`numero_de_cuenta` ASC) VISIBLE,
  CONSTRAINT `cuenta_id_usuario_foreign`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `banco2`.`usuario` (`id_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banco2`.`ubicacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco2`.`ubicacion` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `opcion` ENUM('Cajero', 'Punto fisico') NOT NULL,
  `ciudad` VARCHAR(255) NOT NULL,
  `barrio` VARCHAR(255) NOT NULL,
  `direccion` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banco2`.`retiro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco2`.`retiro` (
  `id_retiro` INT NOT NULL AUTO_INCREMENT,
  `monto_retirar` DECIMAL(15,2) NOT NULL,
  `codigo_retiro` INT NOT NULL,
  `id_ubicacion_retiro` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_retiro`),
  UNIQUE INDEX `retiro_codigo_retiro_unique` (`codigo_retiro` ASC) VISIBLE,
  INDEX `fk_retiro_ubicacion1_idx` (`id_ubicacion_retiro` ASC) VISIBLE,
  CONSTRAINT `fk_retiro_ubicacion1`
    FOREIGN KEY (`id_ubicacion_retiro`)
    REFERENCES `banco2`.`ubicacion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banco2`.`servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco2`.`servicio` (
  `id_servicio` INT NOT NULL AUTO_INCREMENT,
  `nombre` TEXT NOT NULL,
  `costo` DECIMAL(15,2) NOT NULL,
  `descripcion` TEXT NULL,
  `referencia` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id_servicio`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banco2`.`pagos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco2`.`pagos` (
  `id_pagos` INT NOT NULL AUTO_INCREMENT,
  `costo_servicio` DECIMAL(15,2) NOT NULL,
  `id_servicio` INT NOT NULL,
  PRIMARY KEY (`id_pagos`),
  INDEX `fk_pagos_servicio1_idx` (`id_servicio` ASC) VISIBLE,
  CONSTRAINT `fk_pagos_servicio1`
    FOREIGN KEY (`id_servicio`)
    REFERENCES `banco2`.`servicio` (`id_servicio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banco2`.`movimiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco2`.`movimiento` (
  `id_movimiento` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATETIME NOT NULL,
  `id_cuenta` INT NOT NULL,
  `referencia` VARCHAR(255) NOT NULL,
  `id_consignacion` INT NULL,
  `id_retiro` INT NULL,
  `id_pagos` INT NULL,
  PRIMARY KEY (`id_movimiento`),
  UNIQUE INDEX `movimiento_referencia_unique` (`referencia` ASC) VISIBLE,
  INDEX `movimiento_id_consignacion_foreign` (`id_consignacion` ASC) VISIBLE,
  INDEX `movimiento_id_cuenta_foreign` (`id_cuenta` ASC) VISIBLE,
  INDEX `movimiento_id_retiro_foreign` (`id_retiro` ASC) VISIBLE,
  INDEX `fk_movimiento_pagos1_idx` (`id_pagos` ASC) VISIBLE,
  CONSTRAINT `movimiento_id_consignacion_foreign`
    FOREIGN KEY (`id_consignacion`)
    REFERENCES `banco2`.`consignacion` (`id_consignacion`),
  CONSTRAINT `movimiento_id_cuenta_foreign`
    FOREIGN KEY (`id_cuenta`)
    REFERENCES `banco2`.`cuenta` (`id_cuenta`),
  CONSTRAINT `movimiento_id_retiro_foreign`
    FOREIGN KEY (`id_retiro`)
    REFERENCES `banco2`.`retiro` (`id_retiro`),
  CONSTRAINT `fk_movimiento_pagos1`
    FOREIGN KEY (`id_pagos`)
    REFERENCES `banco2`.`pagos` (`id_pagos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


INSERT INTO usuario (tipo_de_id, nombre, apellido, numero_documento, telefono, correo, fecha_nacimiento)
VALUES
('cedula de ciudadania', 'Juan', 'Perez', 1010101010, '3001234567', 'juan.perez@email.com', '1990-01-01'),
('cedula de ciudadania', 'Maria', 'Gomez', 2020202020, '3012345678', 'maria.gomez@email.com', '1992-02-02'),
('cedula de extranjeria', 'Carlos', 'Martinez', 3030303030, '3023456789', 'carlos.martinez@email.com', '1988-03-03'),
('cedula de extranjeria', 'Ana', 'Lopez', 4040404040, '3034567890', 'ana.lopez@email.com', '1995-04-04'),
('pasaporte', 'Luis', 'Garcia', 5050505050, '3045678901', 'luis.garcia@email.com', '1993-05-05'),
('pasaporte', 'Laura', 'Rodriguez', 6060606060, '3056789012', 'laura.rodriguez@email.com', '1991-06-06'),
('cedula de ciudadania', 'Andres', 'Torres', 7070707070, '3067890123', 'andres.torres@email.com', '1989-07-07'),
('cedula de ciudadania', 'Sofia', 'Diaz', 8080808080, '3078901234', 'sofia.diaz@email.com', '1996-08-08'),
('cedula de extranjeria', 'Miguel', 'Ramirez', 9090909090, '3089012345', 'miguel.ramirez@email.com', '1994-09-09'),
('pasaporte', 'Camila', 'Fernandez', 1010101011, '3090123456', 'camila.fernandez@email.com', '1997-10-10');

select * from usuario;

INSERT INTO cuenta (id_usuario, numero_de_cuenta, saldo)
VALUES
(1, '1001-0001', 500000.00),
(2, '1002-0002', 300000.00),
(3, '1003-0003', 700000.00),
(4, '1004-0004', 1000000.00),
(5, '1005-0005', 150000.00),
(6, '1006-0006', 250000.00),
(7, '1007-0007', 350000.00),
(8, '1008-0008', 400000.00),
(9, '1009-0009', 800000.00),
(10, '1010-0010', 450000.00);

select * from cuenta;

INSERT INTO consignacion (telefono_origen, telefono_destino, monto, descripcion, procedencia)
VALUES
(1, 2, 100000.00, 'Consignación de cuenta 1 a 2', 'Corresponsal Bancolombia'),
(2, 3, 200000.00, 'Consignación de cuenta 2 a 3', 'Nequi'),
(3, 4, 50000.00, 'Consignación de cuenta 3 a 4', 'otros Bancos'),
(4, 5, 300000.00, 'Consignación de cuenta 4 a 5', 'Corresponsal Bancolombia'),
(5, 1, 70000.00, 'Consignación de cuenta 5 a 1', 'Nequi'),
(1, 6, 150000.00, 'Consignación de cuenta 1 a 6', 'otros Bancos'),
(2, 7, 40000.00, 'Consignación de cuenta 2 a 7', 'Corresponsal Bancolombia'),
(3, 8, 250000.00, 'Consignación de cuenta 3 a 8', 'Nequi'),
(4, 9, 350000.00, 'Consignación de cuenta 4 a 9', 'otros Bancos'),
(5, 10, 60000.00, 'Consignación de cuenta 5 a 10', 'Nequi');

select * from consignacion;

INSERT INTO ubicacion (nombre, opcion, ciudad, barrio, direccion) 
VALUES
('Cajero Principal', 'Cajero', 'Barranquilla', 'Centro', 'Calle 45 #10-32'),
('Punto Bancario Norte', 'Punto fisico', 'Barranquilla', 'Norte', 'Carrera 52 #80-20'),
('Cajero Express', 'Cajero', 'Bogotá', 'Chapinero', 'Carrera 13 #55-20'),
('Sucursal Sur', 'Punto fisico', 'Bogotá', 'Sur', 'Calle 22B #5-25'),
('Cajero Satélite', 'Cajero', 'Cali', 'Tequendama', 'Calle 9 #25-14'),
('Sucursal Oeste', 'Punto fisico', 'Cali', 'Oeste', 'Avenida 4 Oeste #7-40'),
('Cajero Urbano', 'Cajero', 'Medellín', 'Laureles', 'Carrera 70 #40-10'),
('Punto Físico Centro', 'Punto fisico', 'Medellín', 'Centro', 'Calle 50 #50-20'),
('Cajero Comercial', 'Cajero', 'Cartagena', 'Bocagrande', 'Avenida San Martín #5-30'),
('Sucursal Caribe', 'Punto fisico', 'Cartagena', 'Centro', 'Calle de la Media Luna #3-50');

select * from ubicacion;

INSERT INTO retiro (monto_retirar, codigo_retiro, id_ubicacion_retiro)
VALUES
(100000.00, 1111, 1),
(50000.00, 2222, 2),
(200000.00, 3333, 3),
(70000.00, 4444, 4),
(300000.00, 5555, 5),
(80000.00, 6666, 6),
(60000.00, 7777, 7),
(400000.00, 8888, 8),
(90000.00, 9999, 9),
(10000.00, 1010, 10);

select * from retiro;

INSERT INTO servicio (nombre, costo, descripcion, referencia) 
VALUES
('Claro', 50000.00, 'Compra de paquete de datos o minutos para Claro', 'Referencia_1'),
('Movistar', 60000.00, 'Compra de paquete de datos o minutos para Movistar', 'Referencia_2'),
('Wom', 40000.00, 'Compra de paquete de datos o minutos para Wom', 'Referencia_3'),
('Tigo', 55000.00, 'Compra de paquete de datos o minutos para Tigo', 'Referencia_4'),
('Aires', 30000.00, 'Pago de factura de Aires', 'Referencia_5'),
('AAA', 25000.00, 'Pago de factura de AAA', 'Referencia_6'),
('Claro', 100000.00, 'Compra de paquete de datos o minutos para Claro', 'Referencia_7'),
('Movistar', 120000.00, 'Compra de paquete de datos o minutos para Movistar', 'Referencia_8'),
('Aires', 35000.00, 'Pago de factura de Aires', 'Referencia_9'),
('AAA', 20000.00, 'Pago de factura de AAA', 'Referencia_10');

SELECT * FROM servicio;


INSERT INTO pagos (costo_servicio, id_servicio)
VALUES
(120000.00, 1),
(50000.00, 2),
(300000.00, 3),
(40000.00, 4),
(200000.00, 5),
(80000.00, 6),
(100000.00, 7),
(90000.00, 8),
(70000.00, 9),
(60000.00, 10);

select * from pagos;

INSERT INTO movimiento (fecha, id_cuenta, referencia, id_consignacion, id_retiro, id_pagos)
VALUES
('2024-11-24 08:00:00', 1, 'REF001', 1, NULL, NULL),
('2024-11-24 09:00:00', 2, 'REF002', NULL, 2, NULL),
('2024-11-24 10:00:00', 3, 'REF003', NULL, NULL, 3),
('2024-11-24 11:00:00', 4, 'REF004', 4, NULL, NULL),
('2024-11-24 12:00:00', 5, 'REF005', NULL, 5, NULL),
('2024-11-24 13:00:00', 6, 'REF006', NULL, NULL, 6),
('2024-11-24 14:00:00', 7, 'REF007', 7, NULL, NULL),
('2024-11-24 15:00:00', 8, 'REF008', NULL, 8, NULL),
('2024-11-24 16:00:00', 9, 'REF009', NULL, NULL, 9),
('2024-11-24 17:00:00', 10, 'REF010', 10, NULL, NULL);

select * from movimiento;