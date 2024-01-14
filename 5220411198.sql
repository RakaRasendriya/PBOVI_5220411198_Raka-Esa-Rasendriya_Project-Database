-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2024 at 02:50 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411198`
--

-- --------------------------------------------------------

--
-- Table structure for table `laki`
--

CREATE TABLE `laki` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `top` varchar(255) DEFAULT NULL,
  `bottom` varchar(255) DEFAULT NULL,
  `alas_kaki` varchar(255) DEFAULT NULL,
  `tipe_pakaian` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laki`
--

INSERT INTO `laki` (`id`, `user_id`, `top`, `bottom`, `alas_kaki`, `tipe_pakaian`) VALUES
(1, 1, 'T-shirt ', 'Chino shorts', 'Sneakers', 'casual'),
(2, 3, 'Suit Jacket', 'Chinos', 'Loafers', 'formal'),
(4, 7, 'Hoodie', 'Chino shorts', 'Shoes', 'casual'),
(5, 8, 'Tuxedo shirt', 'Chinos', 'Loafers', 'formal'),
(6, 10, 'Suit Jacket', 'Tuxedo pants', 'Oxford shoes', 'formal');

-- --------------------------------------------------------

--
-- Table structure for table `perempuan`
--

CREATE TABLE `perempuan` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `inner_clothes` varchar(255) DEFAULT NULL,
  `outer_clothes` varchar(255) DEFAULT NULL,
  `bottom` varchar(255) DEFAULT NULL,
  `alas_kaki` varchar(255) DEFAULT NULL,
  `tipe_pakaian` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `perempuan`
--

INSERT INTO `perempuan` (`id`, `user_id`, `inner_clothes`, `outer_clothes`, `bottom`, `alas_kaki`, `tipe_pakaian`) VALUES
(1, 2, 'Kemeja Putih', 'Vest', 'Trousers', 'Slingbacks', 'formal'),
(2, 4, 'T-Shirt', 'Denim Jacket', 'Shorts', 'Sandals', 'casual'),
(4, 9, 'Kemeja Putih', 'Vest', 'Trousers', 'Slingbacks', 'formal'),
(5, 11, 'Blouse', 'Blazer', 'Trousers', 'Pumps', 'formal'),
(6, 12, 'Kemeja Putih', 'Long Cardigan', 'Pencil skirt', 'Heels', 'formal');

-- --------------------------------------------------------

--
-- Table structure for table `tampilan`
--

CREATE TABLE `tampilan` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `aksesoris` varchar(255) DEFAULT NULL,
  `makeup` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tampilan`
--

INSERT INTO `tampilan` (`id`, `user_id`, `aksesoris`, `makeup`) VALUES
(1, 2, 'Anting', 'Skincare-Infused'),
(2, 4, 'Cincin', 'Eye'),
(4, 9, 'Kalung', 'Setting Spray'),
(5, 11, 'Gelang', 'Body'),
(6, 12, 'Gelang', 'Eye');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `umur` int(11) NOT NULL,
  `jenis_kelamin` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `nama`, `umur`, `jenis_kelamin`) VALUES
(1, 'Raka', 20, 'L'),
(2, 'Zaskia', 21, 'P'),
(3, 'Raya', 22, 'L'),
(4, 'Azra', 19, 'P'),
(7, 'Galih', 21, 'L'),
(8, 'Rasya', 25, 'L'),
(9, 'Atika', 20, 'P'),
(10, 'Iqbal', 21, 'L'),
(11, 'Rena', 20, 'P'),
(12, 'Rika', 22, 'P');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `laki`
--
ALTER TABLE `laki`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `perempuan`
--
ALTER TABLE `perempuan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tampilan`
--
ALTER TABLE `tampilan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `laki`
--
ALTER TABLE `laki`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `perempuan`
--
ALTER TABLE `perempuan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tampilan`
--
ALTER TABLE `tampilan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
