-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 01 juil. 2022 à 17:01
-- Version du serveur : 10.4.22-MariaDB
-- Version de PHP : 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `gestion`
--

-- --------------------------------------------------------

--
-- Structure de la table `article`
--

CREATE TABLE `article` (
  `id_article` int(11) NOT NULL,
  `designation` varchar(20) NOT NULL,
  `prix_venter` decimal(10,0) NOT NULL,
  `stock_seuil` int(20) NOT NULL,
  `stock_ini` int(20) NOT NULL,
  `stock_fin` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `article`
--

INSERT INTO `article` (`id_article`, `designation`, `prix_venter`, `stock_seuil`, `stock_ini`, `stock_fin`) VALUES
(1, 'pc', '4000', 20, 50, 50),
(2, 'cyyfc', '5000', 3, 0, 50);

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `code` varchar(20) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `ville` varchar(20) NOT NULL,
  `télephone` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`code`, `nom`, `ville`, `télephone`, `email`, `id`) VALUES
('1', 'ali', 'fes', '0625125565', 'ali.fes@gmail.com', 12),
('2', 'gvucu', 'cucuc', 'ucu', 'gcu', 19);

-- --------------------------------------------------------

--
-- Structure de la table `detai_facture`
--

CREATE TABLE `detai_facture` (
  `id_facture` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `QTE` int(11) NOT NULL,
  `prix` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `detai_facture`
--

INSERT INTO `detai_facture` (`id_facture`, `id_article`, `QTE`, `prix`) VALUES
(1, 1, 4, '4000'),
(2, 1, 1, '4000'),
(3, 2, 10, '5000');

-- --------------------------------------------------------

--
-- Structure de la table `facture_client`
--

CREATE TABLE `facture_client` (
  `id_facture_client` int(11) NOT NULL,
  `date` date NOT NULL,
  `id_client` varchar(20) NOT NULL,
  `montant` decimal(10,2) NOT NULL,
  `mode_pa` varchar(20) NOT NULL,
  `banque` varchar(20) NOT NULL,
  `numero_piece` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `facture_fournisseur`
--

CREATE TABLE `facture_fournisseur` (
  `id_facture_fournisseur` int(11) NOT NULL,
  `date` date NOT NULL,
  `id_fournisseur` int(20) NOT NULL,
  `mantant` decimal(20,0) NOT NULL,
  `mode_pa` varchar(20) NOT NULL,
  `baque` varchar(20) NOT NULL,
  `numero_piece` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `facture_fournisseur`
--

INSERT INTO `facture_fournisseur` (`id_facture_fournisseur`, `date`, `id_fournisseur`, `mantant`, `mode_pa`, `baque`, `numero_piece`) VALUES
(1, '2022-06-15', 1, '2500', '', '', 0),
(2, '2022-06-01', 1, '4000', '', '', 0),
(3, '2022-06-15', 2, '8000', '', '', 0);

-- --------------------------------------------------------

--
-- Structure de la table `fournisseur`
--

CREATE TABLE `fournisseur` (
  `id_fournisseur` int(11) NOT NULL,
  `nom_fournisseur` varchar(20) NOT NULL,
  `tel` varchar(20) NOT NULL,
  `ville` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `credit_initial` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `fournisseur`
--

INSERT INTO `fournisseur` (`id_fournisseur`, `nom_fournisseur`, `tel`, `ville`, `email`, `credit_initial`) VALUES
(1, 'ali', '0625151652', 'casa', 'ali@gmail.com', '5000'),
(2, 'cuct', 'yd', 'ycy', 'vvhiv', '2022');

-- --------------------------------------------------------

--
-- Structure de la table `reglement_client`
--

CREATE TABLE `reglement_client` (
  `id_reglement_client` int(11) NOT NULL,
  `date` date NOT NULL,
  `id_client` int(20) NOT NULL,
  `mantant` decimal(10,0) NOT NULL,
  `mode` varchar(20) NOT NULL,
  `banque` varchar(20) NOT NULL,
  `numero_piece` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `reglement_fournisseur`
--

CREATE TABLE `reglement_fournisseur` (
  `id_reglement_fournisseur` int(11) NOT NULL,
  `date` date NOT NULL,
  `id_fournisseur` int(10) NOT NULL,
  `mantant` decimal(10,0) NOT NULL,
  `mode_pe` varchar(20) NOT NULL,
  `banque` varchar(20) NOT NULL,
  `numero_piece` mediumint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `login` varchar(56) NOT NULL,
  `password` varchar(36) NOT NULL,
  `niveau` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `login`, `password`, `niveau`) VALUES
(1, 'admin', '123', 'Administrateur'),
(2, 'ggg', '250', '');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`id_article`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `facture_client`
--
ALTER TABLE `facture_client`
  ADD PRIMARY KEY (`id_facture_client`);

--
-- Index pour la table `facture_fournisseur`
--
ALTER TABLE `facture_fournisseur`
  ADD PRIMARY KEY (`id_facture_fournisseur`),
  ADD UNIQUE KEY `id_facture_3` (`id_facture_fournisseur`),
  ADD KEY `id_facture` (`id_facture_fournisseur`),
  ADD KEY `id_facture_2` (`id_facture_fournisseur`);

--
-- Index pour la table `fournisseur`
--
ALTER TABLE `fournisseur`
  ADD PRIMARY KEY (`id_fournisseur`);

--
-- Index pour la table `reglement_client`
--
ALTER TABLE `reglement_client`
  ADD PRIMARY KEY (`id_reglement_client`);

--
-- Index pour la table `reglement_fournisseur`
--
ALTER TABLE `reglement_fournisseur`
  ADD PRIMARY KEY (`id_reglement_fournisseur`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `article`
--
ALTER TABLE `article`
  MODIFY `id_article` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `client`
--
ALTER TABLE `client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT pour la table `facture_client`
--
ALTER TABLE `facture_client`
  MODIFY `id_facture_client` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `facture_fournisseur`
--
ALTER TABLE `facture_fournisseur`
  MODIFY `id_facture_fournisseur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `fournisseur`
--
ALTER TABLE `fournisseur`
  MODIFY `id_fournisseur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `reglement_client`
--
ALTER TABLE `reglement_client`
  MODIFY `id_reglement_client` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `reglement_fournisseur`
--
ALTER TABLE `reglement_fournisseur`
  MODIFY `id_reglement_fournisseur` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
