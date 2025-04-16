-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 16, 2025 at 03:10 AM
-- Server version: 8.0.41-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs432g11`
--

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int NOT NULL,
  `member_id` int NOT NULL,
  `outlet_id` int NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `order_status` enum('Pending','Completed','Cancelled') DEFAULT 'Pending',
  `order_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `payment_method` varchar(50) DEFAULT 'UPI'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `member_id`, `outlet_id`, `total_amount`, `order_status`, `order_time`, `payment_method`) VALUES
(1, 2160, 1, '290.00', 'Pending', '2025-04-16 00:04:03', 'UPI'),
(2, 2160, 1, '290.00', 'Pending', '2025-04-16 00:09:28', 'UPI'),
(3, 2160, 1, '530.00', 'Completed', '2025-04-16 01:40:06', 'UPI'),
(4, 2160, 2, '140.00', 'Completed', '2025-04-16 00:40:34', 'UPI'),
(5, 2160, 1, '220.00', 'Pending', '2025-04-15 16:24:55', 'UPI'),
(6, 2160, 1, '440.00', 'Pending', '2025-04-15 16:29:35', 'UPI'),
(7, 2163, 6, '50.00', 'Pending', '2025-04-15 16:36:45', 'UPI'),
(8, 2163, 2, '65.00', 'Pending', '2025-04-15 16:37:59', 'UPI'),
(9, 2163, 4, '60.00', 'Pending', '2025-04-15 17:33:53', 'UPI'),
(10, 2163, 4, '35.00', 'Pending', '2025-04-15 17:35:35', 'UPI'),
(11, 2163, 2, '35.00', 'Pending', '2025-04-15 17:41:07', 'UPI'),
(12, 2163, 6, '50.00', 'Pending', '2025-04-15 18:21:46', 'UPI'),
(13, 2163, 5, '85.00', 'Pending', '2025-04-15 18:35:49', 'UPI'),
(14, 2163, 1, '420.00', 'Pending', '2025-04-15 22:35:08', 'UPI'),
(15, 2163, 4, '240.00', 'Pending', '2025-04-15 22:38:37', 'UPI'),
(16, 2163, 1, '150.00', 'Pending', '2025-04-15 22:39:52', 'UPI'),
(17, 2163, 3, '5.00', 'Pending', '2025-04-16 04:08:01', 'UPI'),
(18, 2160, 1, '250.00', 'Pending', '2025-04-16 04:44:49', 'UPI'),
(19, 2160, 1, '250.00', 'Pending', '2025-04-16 04:44:51', 'UPI'),
(20, 2163, 5, '100.00', 'Pending', '2025-04-16 04:45:53', 'UPI'),
(21, 2163, 6, '70.00', 'Pending', '2025-04-16 04:49:06', 'UPI'),
(22, 2163, 4, '30.00', 'Cancelled', '2025-04-16 04:55:15', 'UPI'),
(23, 2163, 2, '120.00', 'Pending', '2025-04-16 05:11:57', 'UPI'),
(24, 2163, 1, '40.00', 'Pending', '2025-04-16 05:19:53', 'UPI'),
(25, 2163, 4, '30.00', 'Pending', '2025-04-16 05:28:04', 'UPI'),
(26, 2163, 6, '120.00', 'Pending', '2025-04-16 06:53:08', 'UPI'),
(27, 2160, 4, '190.00', 'Completed', '2025-04-16 07:01:25', 'UPI'),
(28, 2160, 1, '170.00', 'Pending', '2025-04-16 07:01:29', 'UPI'),
(29, 2160, 4, '190.00', 'Completed', '2025-04-16 07:07:29', 'UPI'),
(30, 2160, 1, '170.00', 'Pending', '2025-04-16 07:07:34', 'UPI');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `outlet_id` (`outlet_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`outlet_id`) REFERENCES `outlet` (`outlet_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
