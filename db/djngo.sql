-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 03-04-2024 a las 16:05:31
-- Versión del servidor: 8.0.30
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `djngo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add bookmark', 7, 'add_bookmark'),
(26, 'Can change bookmark', 7, 'change_bookmark'),
(27, 'Can delete bookmark', 7, 'delete_bookmark'),
(28, 'Can view bookmark', 7, 'view_bookmark'),
(29, 'Can add pinned application', 8, 'add_pinnedapplication'),
(30, 'Can change pinned application', 8, 'change_pinnedapplication'),
(31, 'Can delete pinned application', 8, 'delete_pinnedapplication'),
(32, 'Can view pinned application', 8, 'view_pinnedapplication');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$AVvS8kgCMiuoc2OYCbBrXA$n3XGxbqG6QFKc6SvO8TuwOSO3GvGsvWb2E64gVZlQ/8=', '2024-04-03 12:35:42.784694', 0, 'usuario', 'Usuario', 'Usuario', 'usuario@admin.com', 0, 1, '2024-03-31 12:12:40.000000'),
(2, 'pbkdf2_sha256$260000$F9n7gd6ryDZ2FVF6Xj0wKW$+hhGkBdoG5L4Xx9rvOWGkFGVhIAa6hzYYL/laNHlb4c=', '2024-04-02 11:15:15.962169', 1, 'dm', '', '', 'admin@admin.com', 1, 1, '2024-03-31 13:46:00.795739'),
(3, 'pbkdf2_sha256$260000$F9n7gd6ryDZ2FVF6Xj0wKW$+hhGkBdoG5L4Xx9rvOWGkFGVhIAa6hzYYL/laNHlb4c=', '2024-04-03 13:24:58.350619', 0, 'admin', '', '', 'admin@gmail.com', 1, 1, '2024-03-31 19:49:58.598251');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-04-02 12:39:25.912008', '1', 'admin', 2, '[]', 4, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'jet', 'bookmark'),
(8, 'jet', 'pinnedapplication'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-03-31 12:09:42.951120'),
(2, 'auth', '0001_initial', '2024-03-31 12:09:43.419840'),
(3, 'admin', '0001_initial', '2024-03-31 12:09:43.576079'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-03-31 12:09:43.591702'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-31 12:09:43.591702'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-03-31 12:09:43.685446'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-03-31 12:09:43.732321'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-03-31 12:09:43.779191'),
(9, 'auth', '0004_alter_user_username_opts', '2024-03-31 12:09:43.779191'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-03-31 12:09:43.841685'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-03-31 12:09:43.841685'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-03-31 12:09:43.857316'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-03-31 12:09:43.904180'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-03-31 12:09:43.951054'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-03-31 12:09:43.982307'),
(16, 'auth', '0011_update_proxy_permissions', '2024-03-31 12:09:43.997925'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-03-31 12:09:44.044797'),
(18, 'sessions', '0001_initial', '2024-03-31 12:09:44.091675'),
(19, 'jet', '0001_initial', '2024-04-02 11:53:34.540704'),
(20, 'jet', '0002_delete_userdashboardmodule', '2024-04-02 11:53:34.556329');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4o3q7b52xn4udg0iplirlpk2u903l7pd', '.eJxVjMsOwiAQRf-FtSHDowVcuvcbCMMMUjU0Ke3K-O_apAvd3nPOfYmYtrXGrfMSJxJnocTpd8OUH9x2QPfUbrPMc1uXCeWuyIN2eZ2Jn5fD_TuoqddvDZ7IFgBCVRiYEB3qktm4wXm21mZiBpWNScUr1IFGCmEoBrTJYVTi_QER1DiM:1rqvhj:_FpX_tK5Vrtop8LUQyCAJdG159S9euFYGkqZt0Be18g', '2024-04-14 13:58:35.032621'),
('69q6q4j9eqnkxou284ton8k6pc7421qz', 'e30:1rrzZx:WXs6pV6fQKCbbE1HmnTxAqRL-K_vPMdGlY-W_uvZQeA', '2024-04-17 12:18:57.677996'),
('6fy6g4bt8leconepvcrsl2lu8gz933mt', '.eJxVjMsOwiAQRf-FtSHDowVcuvcbCMMMUjU0Ke3K-O_apAvd3nPOfYmYtrXGrfMSJxJnocTpd8OUH9x2QPfUbrPMc1uXCeWuyIN2eZ2Jn5fD_TuoqddvDZ7IFgBCVRiYEB3qktm4wXm21mZiBpWNScUr1IFGCmEoBrTJYVTi_QER1DiM:1rr1VM:YX7___ycV1STBNDLCp0_8LRvT-rmdbCIo75ZFID8p8o', '2024-04-14 20:10:12.748813'),
('kwsnyetadkyrie6n8jmldu62rp5a3da0', '.eJxVjE0OwiAYBe_C2hB-W3Dp3jOQD3iVqoGktCvj3bVJF7p9M_NeLNC2lrB1LGHO7MwUO_1ukdIDdQf5TvXWeGp1XebId4UftPNry3heDvfvoFAv39pk53US1smIpCCkHy0MJZOjgFXZOUsjvJEYBEEKk6ZIIEBqMUxGs_cH6T84Ug:1rrSiN:c9H-xbGWvliOxOu5hY5xKc2GkYFZtoA3AbuXhetx5Bc', '2024-04-16 01:13:27.147148');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `etapas`
--

CREATE TABLE `etapas` (
  `id` int NOT NULL,
  `id_user` int DEFAULT NULL,
  `fecha_etapa` date DEFAULT NULL,
  `tipo_etapa` tinyint(1) DEFAULT NULL,
  `status_etapa` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `etapas`
--

INSERT INTO `etapas` (`id`, `id_user`, `fecha_etapa`, `tipo_etapa`, `status_etapa`) VALUES
(1, 1, '2023-12-01', 1, 1),
(2, 1, '2023-12-04', 2, 1),
(3, 1, '2024-04-03', 3, 1),
(4, 1, '2023-12-31', 4, 0),
(5, 1, '2024-06-07', 5, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jet_bookmark`
--

CREATE TABLE `jet_bookmark` (
  `id` int NOT NULL,
  `url` varchar(200) NOT NULL,
  `title` varchar(255) NOT NULL,
  `user` int UNSIGNED NOT NULL,
  `date_add` datetime(6) NOT NULL
) ;

--
-- Volcado de datos para la tabla `jet_bookmark`
--

INSERT INTO `jet_bookmark` (`id`, `url`, `title`, `user`, `date_add`) VALUES
(3, 'http://127.0.0.1:8000/etapa_id/', 'Etapas', 2, '2024-04-02 12:44:30.590564');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jet_pinnedapplication`
--

CREATE TABLE `jet_pinnedapplication` (
  `id` int NOT NULL,
  `app_label` varchar(255) NOT NULL,
  `user` int UNSIGNED NOT NULL,
  `date_add` datetime(6) NOT NULL
) ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `etapas`
--
ALTER TABLE `etapas`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- Indices de la tabla `jet_bookmark`
--
ALTER TABLE `jet_bookmark`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `jet_pinnedapplication`
--
ALTER TABLE `jet_pinnedapplication`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `etapas`
--
ALTER TABLE `etapas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `jet_bookmark`
--
ALTER TABLE `jet_bookmark`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `jet_pinnedapplication`
--
ALTER TABLE `jet_pinnedapplication`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
