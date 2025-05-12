CREATE TABLE IF NOT EXISTS carrito (
    id_carrito INT AUTO_INCREMENT NOT NULL,
    fecha DATE,
    usuariosid_usuario INT NOT NULL,
    PRIMARY KEY (id_carrito)
);

CREATE TABLE IF NOT EXISTS detalle_carrito (
    juegoid INT NOT NULL,
    carritoid_carrito INT NOT NULL,
    cantidad INT,
    PRIMARY KEY (juegoid, carritoid_carrito)
);

CREATE TABLE IF NOT EXISTS detalle_venta (
    carritoid_carrito INT NOT NULL,
    ventaid_venta INT NOT NULL,
    total_venta DECIMAL(10, 2),
    PRIMARY KEY (carritoid_carrito, ventaid_venta)
);

CREATE TABLE IF NOT EXISTS favorito (
    id_favoritos INT AUTO_INCREMENT NOT NULL,
    usuariosid_usuario INT NOT NULL,
    juegoid INT NOT NULL,
    PRIMARY KEY (id_favoritos)
);

CREATE TABLE IF NOT EXISTS genero (
    id_genero INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(100),
    descripcion VARCHAR(100),
    PRIMARY KEY (id_genero)
);

CREATE TABLE IF NOT EXISTS juego (
    id INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(100),
    precio DECIMAL(10, 2),
    estado TINYINT(1),
    imagen text,
    imagene1 text,
    imagene2 text,
    imagene3 text,
    cantidad INT,
    descripcion_juego VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS juego_genero (
    juegoid INT NOT NULL,
    generoid_genero INT NOT NULL,
    PRIMARY KEY (juegoid, generoid_genero)
);

CREATE TABLE IF NOT EXISTS llave (
    id_llave INT AUTO_INCREMENT NOT NULL,
    codigo_llave INT,
    vigencia TINYINT(1),
    juegoid INT NOT NULL,
    PRIMARY KEY (id_llave)
);

CREATE TABLE IF NOT EXISTS rol (
    id_rol INT AUTO_INCREMENT NOT NULL,
    nombre_rol VARCHAR(100),
    PRIMARY KEY (id_rol)
);

CREATE TABLE IF NOT EXISTS tarjeta (
    id_tarjeta INT AUTO_INCREMENT NOT NULL,
    numero_tarjeta VARCHAR(16),
    ccv VARCHAR(3),
    ciudad VARCHAR(100),
    fecha_expiracion DATE,
    tipo TINYINT(1),
    usuariosid_usuario INT NOT NULL,
    PRIMARY KEY (id_tarjeta)
);

CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT AUTO_INCREMENT NOT NULL,
    nombre_usuario VARCHAR(50),
    correo VARCHAR(255),
    genero TINYINT(1),
    contraseña VARCHAR(100),
    telefono VARCHAR(9),
    pais VARCHAR(100),
    fecha_nacimiento date,
    rolid_rol INT NOT NULL,
    foto_perfil text,
    foto_portada text,
    PRIMARY KEY (id_usuario)
);

CREATE TABLE IF NOT EXISTS venta (
    id_venta INT AUTO_INCREMENT NOT NULL,
    fecha DATE,
    PRIMARY KEY (id_venta)
);
