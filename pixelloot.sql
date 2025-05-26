-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-05-2025 a las 06:46:38
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pixelloot`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `id_carrito` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `usuariosid_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`id_carrito`, `fecha`, `usuariosid_usuario`) VALUES
(1, '2025-05-24', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_carrito`
--

CREATE TABLE `detalle_carrito` (
  `juegoid` int(11) NOT NULL,
  `carritoid_carrito` int(11) NOT NULL,
  `cantidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalle_carrito`
--

INSERT INTO `detalle_carrito` (`juegoid`, `carritoid_carrito`, `cantidad`) VALUES
(1, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_venta`
--

CREATE TABLE `detalle_venta` (
  `carritoid_carrito` int(11) NOT NULL,
  `ventaid_venta` int(11) NOT NULL,
  `total_venta` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalle_venta`
--

INSERT INTO `detalle_venta` (`carritoid_carrito`, `ventaid_venta`, `total_venta`) VALUES
(1, 1, 143.37);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favorito`
--

CREATE TABLE `favorito` (
  `id_favoritos` int(11) NOT NULL,
  `usuariosid_usuario` int(11) NOT NULL,
  `juegoid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id_genero` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `juego`
--

CREATE TABLE `juego` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `imagen` text DEFAULT NULL,
  `imagene1` text DEFAULT NULL,
  `imagene2` text DEFAULT NULL,
  `imagene3` text DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `descripcion_juego` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `juego`
--

INSERT INTO `juego` (`id`, `nombre`, `precio`, `estado`, `imagen`, `imagene1`, `imagene2`, `imagene3`, `cantidad`, `descripcion_juego`) VALUES
(1, 'God of War', 159.30, 1, 'static/imagenes\\1.jpg', 'imagenes/Screen Game/1/god_1.jpg', 'imagenes/Screen Game/1/god_2.jpg', 'imagenes/Screen Game/1/god_3.jpg', 11, 'pueba');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `juego_genero`
--

CREATE TABLE `juego_genero` (
  `juegoid` int(11) NOT NULL,
  `generoid_genero` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `llave`
--

CREATE TABLE `llave` (
  `id_llave` int(11) NOT NULL,
  `codigo_llave` int(11) DEFAULT NULL,
  `vigencia` tinyint(1) DEFAULT NULL,
  `juegoid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id_rol` int(11) NOT NULL,
  `nombre_rol` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id_rol`, `nombre_rol`) VALUES
(1, 'Usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tarjeta`
--

CREATE TABLE `tarjeta` (
  `id_tarjeta` int(11) NOT NULL,
  `numero_tarjeta` varchar(16) DEFAULT NULL,
  `ccv` varchar(3) DEFAULT NULL,
  `ciudad` varchar(100) DEFAULT NULL,
  `fecha_expiracion` varchar(7) DEFAULT NULL,
  `tipo` char(1) DEFAULT NULL,
  `usuariosid_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tarjeta`
--

INSERT INTO `tarjeta` (`id_tarjeta`, `numero_tarjeta`, `ccv`, `ciudad`, `fecha_expiracion`, `tipo`, `usuariosid_usuario`) VALUES
(5, '4234324332443243', '123', 'Chiclayo', '2029-02', '0', 10),
(6, '1222222222222222', '123', 'Chiclayo', '2025-03', '1', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(50) DEFAULT NULL,
  `nombre_real` varchar(100) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `genero` tinyint(1) DEFAULT NULL,
  `contraseña` varchar(100) DEFAULT NULL,
  `telefono` varchar(9) DEFAULT NULL,
  `pais` varchar(100) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `rolid_rol` int(11) NOT NULL,
  `foto_perfil` text DEFAULT NULL,
  `foto_portada` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nombre_usuario`, `nombre_real`, `correo`, `genero`, `contraseña`, `telefono`, `pais`, `fecha_nacimiento`, `rolid_rol`, `foto_perfil`, `foto_portada`) VALUES
(10, 'JESH', 'Jorge', 'asd@hotmial.com', 0, 'lol', '968543548', 'Perú', '2025-06-04', 1, 'static/imagenes/MenuPrincipalyPerfil/perfil.jpg', 'static/imagenes/MenuPrincipalyPerfil/fondoPerfilAuto.jpg'),
(13, 'asdasd', 'asd', 'asd@hotmial.com', 0, 'asd', '1231231', 'Perú', '2025-05-20', 1, 'static/imagenes/MenuPrincipalyPerfil/perfil.jpg', 'static/imagenes/MenuPrincipalyPerfil/fondoPerfilAuto.jpg'),
(14, 'locaso', 'Jorfge', 'asd@asd', 0, '1234', '1231231', 'Brasil', '2025-04-03', 1, 'static/imagenes/MenuPrincipalyPerfil/perfil.jpg', 'static/imagenes/MenuPrincipalyPerfil/fondoPerfilAuto.jpg'),
(15, 'asdasd', 'asd', 'asd@hotmial.com', 0, '111', '968543548', 'Perú', '2025-04-30', 1, 'static/imagenes/MenuPrincipalyPerfil/perfil.jpg', 'static/imagenes/MenuPrincipalyPerfil/fondoPerfilAuto.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `id_venta` int(11) NOT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`id_venta`, `fecha`) VALUES
(1, '2025-05-24');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`id_carrito`),
  ADD KEY `fk_carrito_usuario` (`usuariosid_usuario`);

--
-- Indices de la tabla `detalle_carrito`
--
ALTER TABLE `detalle_carrito`
  ADD PRIMARY KEY (`juegoid`,`carritoid_carrito`),
  ADD KEY `fk_detalle_carrito_carrito` (`carritoid_carrito`);

--
-- Indices de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD PRIMARY KEY (`carritoid_carrito`,`ventaid_venta`),
  ADD KEY `fk_detalle_venta_venta` (`ventaid_venta`);

--
-- Indices de la tabla `favorito`
--
ALTER TABLE `favorito`
  ADD PRIMARY KEY (`id_favoritos`),
  ADD KEY `fk_favorito_usuario` (`usuariosid_usuario`),
  ADD KEY `fk_favorito_juego` (`juegoid`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id_genero`);

--
-- Indices de la tabla `juego`
--
ALTER TABLE `juego`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `juego_genero`
--
ALTER TABLE `juego_genero`
  ADD PRIMARY KEY (`juegoid`,`generoid_genero`),
  ADD KEY `fk_juego_genero_genero` (`generoid_genero`);

--
-- Indices de la tabla `llave`
--
ALTER TABLE `llave`
  ADD PRIMARY KEY (`id_llave`),
  ADD KEY `fk_llave_juego` (`juegoid`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  ADD PRIMARY KEY (`id_tarjeta`),
  ADD KEY `fk_tarjeta_usuario` (`usuariosid_usuario`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `fk_usuario_rol` (`rolid_rol`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`id_venta`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carrito`
--
ALTER TABLE `carrito`
  MODIFY `id_carrito` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `favorito`
--
ALTER TABLE `favorito`
  MODIFY `id_favoritos` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id_genero` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `juego`
--
ALTER TABLE `juego`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `llave`
--
ALTER TABLE `llave`
  MODIFY `id_llave` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  MODIFY `id_tarjeta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
  MODIFY `id_venta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD CONSTRAINT `fk_carrito_usuario` FOREIGN KEY (`usuariosid_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `detalle_carrito`
--
ALTER TABLE `detalle_carrito`
  ADD CONSTRAINT `fk_detalle_carrito_carrito` FOREIGN KEY (`carritoid_carrito`) REFERENCES `carrito` (`id_carrito`),
  ADD CONSTRAINT `fk_detalle_carrito_juego` FOREIGN KEY (`juegoid`) REFERENCES `juego` (`id`);

--
-- Filtros para la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD CONSTRAINT `fk_detalle_venta_carrito` FOREIGN KEY (`carritoid_carrito`) REFERENCES `carrito` (`id_carrito`),
  ADD CONSTRAINT `fk_detalle_venta_venta` FOREIGN KEY (`ventaid_venta`) REFERENCES `venta` (`id_venta`);

--
-- Filtros para la tabla `favorito`
--
ALTER TABLE `favorito`
  ADD CONSTRAINT `fk_favorito_juego` FOREIGN KEY (`juegoid`) REFERENCES `juego` (`id`),
  ADD CONSTRAINT `fk_favorito_usuario` FOREIGN KEY (`usuariosid_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `juego_genero`
--
ALTER TABLE `juego_genero`
  ADD CONSTRAINT `fk_juego_genero_genero` FOREIGN KEY (`generoid_genero`) REFERENCES `genero` (`id_genero`),
  ADD CONSTRAINT `fk_juego_genero_juego` FOREIGN KEY (`juegoid`) REFERENCES `juego` (`id`);

--
-- Filtros para la tabla `llave`
--
ALTER TABLE `llave`
  ADD CONSTRAINT `fk_llave_juego` FOREIGN KEY (`juegoid`) REFERENCES `juego` (`id`);

--
-- Filtros para la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  ADD CONSTRAINT `fk_tarjeta_usuario` FOREIGN KEY (`usuariosid_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_usuario_rol` FOREIGN KEY (`rolid_rol`) REFERENCES `rol` (`id_rol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
