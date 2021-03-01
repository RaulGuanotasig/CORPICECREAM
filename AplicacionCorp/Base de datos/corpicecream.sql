-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-09-2020 a las 21:05:16
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `corpicecream`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
  `id_adm` int(11) NOT NULL,
  `usuario_adm` varchar(50) DEFAULT NULL,
  `password_adm` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`id_adm`, `usuario_adm`, `password_adm`) VALUES
(1, 'a', 'a'),
(2, 'a', 'a'),
(3, 'operador', '1234'),
(4, 'operador', '1234'),
(5, 'operador', '1234');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calculocontable`
--

CREATE TABLE `calculocontable` (
  `id_cal` int(11) NOT NULL,
  `anioInicial` int(11) DEFAULT NULL,
  `mesInicial` int(11) DEFAULT NULL,
  `anioFinal` int(11) DEFAULT NULL,
  `mesFinal` int(11) DEFAULT NULL,
  `valor_cal` float DEFAULT NULL,
  `porcentajeDepr_cal` float DEFAULT NULL,
  `anioCompra_cal` int(11) DEFAULT NULL,
  `costoA_cal` float DEFAULT NULL,
  `costo_cal` float DEFAULT NULL,
  `vidaUtil_cal` int(11) DEFAULT NULL,
  `mesAcumuladoI_cal` int(11) DEFAULT NULL,
  `depreciacionAcumuladaI_cal` float DEFAULT NULL,
  `meses_cal` int(11) DEFAULT NULL,
  `gasto_cal` float DEFAULT NULL,
  `mesAcumuladoH_cal` int(11) DEFAULT NULL,
  `depreciacionAcumuladaH_cal` float DEFAULT NULL,
  `depreciacionAcumuladaV_cal` float DEFAULT NULL,
  `saldoLibros_cal` float DEFAULT NULL,
  `id_rep1` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `control`
--

CREATE TABLE `control` (
  `id_con` int(11) NOT NULL,
  `mesCompra_con` varchar(50) DEFAULT NULL,
  `compraXII_con` float DEFAULT NULL,
  `compraXIIAF_con` float DEFAULT NULL,
  `comprasSinCtrib_con` float DEFAULT NULL,
  `importacionesXII_con` float DEFAULT NULL,
  `importacionesXIIAF_con` float DEFAULT NULL,
  `reembolso_con` float DEFAULT NULL,
  `totalComprasXII_con` float DEFAULT NULL,
  `totalComprasO_con` float DEFAULT NULL,
  `noObjIva_con` float DEFAULT NULL,
  `ivaXIIConImporta_con` float DEFAULT NULL,
  `ivaXIISinImport_con` float DEFAULT NULL,
  `fecha_compradepm_ges` int(11) DEFAULT NULL,
  `depreciacion` float(20,2) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `mes_acumulado` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `control`
--

INSERT INTO `control` (`id_con`, `mesCompra_con`, `compraXII_con`, `compraXIIAF_con`, `comprasSinCtrib_con`, `importacionesXII_con`, `importacionesXIIAF_con`, `reembolso_con`, `totalComprasXII_con`, `totalComprasO_con`, `noObjIva_con`, `ivaXIIConImporta_con`, `ivaXIISinImport_con`, `fecha_compradepm_ges`, `depreciacion`, `tipo`, `mes_acumulado`) VALUES
(13, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 449.25, 'TERRENOS', 80),
(14, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 449.25, 'EDIFICIOS', 80),
(15, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 449.25, 'EDIFICIOS', 80);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestiondatos`
--

CREATE TABLE `gestiondatos` (
  `id_ges` int(11) NOT NULL,
  `nombregru_ges` varchar(50) DEFAULT NULL,
  `cantidad_ges` int(11) DEFAULT NULL,
  `descripcionDelBien_ges` varchar(50) DEFAULT NULL,
  `modelo_ges` varchar(50) DEFAULT NULL,
  `proveedor_ges` varchar(50) DEFAULT NULL,
  `factura_ges` varchar(50) DEFAULT NULL,
  `vidaUtil_ges` int(11) DEFAULT NULL,
  `edad_ges` int(11) DEFAULT NULL,
  `edadPro_ges` int(11) DEFAULT NULL,
  `residual_ges` int(11) DEFAULT NULL,
  `costoHistorico_ges` float DEFAULT NULL,
  `fechaCompraa_ges` int(11) DEFAULT NULL,
  `fechaCompram_ges` int(11) DEFAULT NULL,
  `fechaComprad_ges` int(11) DEFAULT NULL,
  `fecha_Compradepa_ges` int(11) DEFAULT NULL,
  `fecha_Compradepm_ges` int(11) DEFAULT NULL,
  `id_adm1` int(11) DEFAULT NULL,
  `id_con1` int(11) DEFAULT NULL,
  `id_cal1` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `gestiondatos`
--

INSERT INTO `gestiondatos` (`id_ges`, `nombregru_ges`, `cantidad_ges`, `descripcionDelBien_ges`, `modelo_ges`, `proveedor_ges`, `factura_ges`, `vidaUtil_ges`, `edad_ges`, `edadPro_ges`, `residual_ges`, `costoHistorico_ges`, `fechaCompraa_ges`, `fechaCompram_ges`, `fechaComprad_ges`, `fecha_Compradepa_ges`, `fecha_Compradepm_ges`, `id_adm1`, `id_con1`, `id_cal1`) VALUES
(69, 'TERRENOS', 0, 'Ubicado en salcedo', '', '', '', 20, 2, 95, 0, 533.48, 2012, 4, 11, 2018, 12, NULL, NULL, NULL),
(70, 'EDIFICIOS', 0, 'En construccion', '', '', '', 15, 1, 95, 0, 533.48, 2012, 4, 11, 2018, 12, NULL, NULL, NULL),
(71, 'EDIFICIOS', 0, '', '', '', '', 20, 2, 95, 0, 533.48, 2012, 4, 22, 2018, 12, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reporte`
--

CREATE TABLE `reporte` (
  `id_rep` int(11) NOT NULL,
  `descargar_rep` mediumblob DEFAULT NULL,
  `visualizar_rep` mediumblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`id_adm`);

--
-- Indices de la tabla `calculocontable`
--
ALTER TABLE `calculocontable`
  ADD PRIMARY KEY (`id_cal`),
  ADD KEY `id_rep1` (`id_rep1`);

--
-- Indices de la tabla `control`
--
ALTER TABLE `control`
  ADD PRIMARY KEY (`id_con`);

--
-- Indices de la tabla `gestiondatos`
--
ALTER TABLE `gestiondatos`
  ADD PRIMARY KEY (`id_ges`),
  ADD KEY `id_adm1` (`id_adm1`),
  ADD KEY `id_con1` (`id_con1`),
  ADD KEY `id_cal1` (`id_cal1`);

--
-- Indices de la tabla `reporte`
--
ALTER TABLE `reporte`
  ADD PRIMARY KEY (`id_rep`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador`
--
ALTER TABLE `administrador`
  MODIFY `id_adm` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `calculocontable`
--
ALTER TABLE `calculocontable`
  MODIFY `id_cal` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `control`
--
ALTER TABLE `control`
  MODIFY `id_con` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `gestiondatos`
--
ALTER TABLE `gestiondatos`
  MODIFY `id_ges` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT de la tabla `reporte`
--
ALTER TABLE `reporte`
  MODIFY `id_rep` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `calculocontable`
--
ALTER TABLE `calculocontable`
  ADD CONSTRAINT `calculocontable_ibfk_1` FOREIGN KEY (`id_rep1`) REFERENCES `reporte` (`id_rep`);

--
-- Filtros para la tabla `gestiondatos`
--
ALTER TABLE `gestiondatos`
  ADD CONSTRAINT `gestiondatos_ibfk_1` FOREIGN KEY (`id_adm1`) REFERENCES `administrador` (`id_adm`),
  ADD CONSTRAINT `gestiondatos_ibfk_2` FOREIGN KEY (`id_con1`) REFERENCES `control` (`id_con`),
  ADD CONSTRAINT `gestiondatos_ibfk_3` FOREIGN KEY (`id_cal1`) REFERENCES `calculocontable` (`id_cal`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
