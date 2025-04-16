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
-- Database: `cs432cims`
--
CREATE DATABASE IF NOT EXISTS `cs432cims` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `cs432cims`;

-- --------------------------------------------------------

--
-- Table structure for table `G1_report_analytics`
--

CREATE TABLE `G1_report_analytics` (
  `Report_ID` int NOT NULL,
  `Report_Type` varchar(100) NOT NULL,
  `Generated_On` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `G1_report_analytics`
--

INSERT INTO `G1_report_analytics` (`Report_ID`, `Report_Type`, `Generated_On`) VALUES
(1, '1', '2025-04-15 20:00:06'),
(2, '1', '2025-04-15 20:00:34'),
(3, 'Seller Summary Report', '2025-04-15 20:01:15'),
(4, 'Seller Summary Report', '2025-04-15 20:01:15'),
(5, 'Seller Summary Report', '2025-04-15 22:26:54'),
(6, 'Seller Summary Report', '2025-04-15 22:26:54'),
(7, 'Seller Summary Report', '2025-04-16 01:13:39'),
(8, 'Seller Summary Report', '2025-04-16 01:13:39'),
(9, 'Seller Summary Report', '2025-04-16 02:09:29'),
(10, 'Seller Summary Report', '2025-04-16 02:09:29'),
(11, 'Seller Summary Report', '2025-04-16 04:47:52'),
(12, 'Seller Summary Report', '2025-04-16 04:47:52'),
(13, 'Seller Summary Report', '2025-04-16 05:48:13'),
(14, 'Seller Summary Report', '2025-04-16 05:48:13');

-- --------------------------------------------------------

--
-- Table structure for table `G2_Venue`
--

CREATE TABLE `G2_Venue` (
  `VenueID` int NOT NULL,
  `VenueName` varchar(255) NOT NULL,
  `Location` varchar(255) NOT NULL,
  `Sport` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `G3_job_desc`
--

CREATE TABLE `G3_job_desc` (
  `Discipline_name` varchar(60) NOT NULL,
  `Designation` varchar(80) NOT NULL,
  `Room_number` varchar(5) NOT NULL,
  `Building` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `G3_job_desc`
--

INSERT INTO `G3_job_desc` (`Discipline_name`, `Designation`, `Room_number`, `Building`) VALUES
('Materials Management', 'Junior Accounts Officer', '111E', 'AB3'),
('Estate and Works', 'Junior Laboratory Attendant', '202', 'AB3'),
('Physics', 'Professor', '207A', 'AB10'),
('Materials Engineering', 'Associate Professor', '306A', 'AB11'),
('Physics', 'Associate Professor', '307A', 'AB10'),
('Hospitality', 'Junior Accounts Assistant', '308', 'AB3'),
('Physics', 'Associate Professor', '310A', 'AB10'),
('Junior Laboratory Assistant', 'Campus Development', '311', 'AB3'),
('Mechanical Engineering', 'Assistant Professor', '315B', 'AB12'),
('Electrical Engineering', 'Associate Professor', '327C', 'AB13'),
('Hospitality', 'Hospitality Manager', '329', 'AB3'),
('Computer Science and Engineering', 'Assistant Professor', '403B', 'AB13'),
('Computer Science and Engineering', 'Assistant Professor', '405A', 'AB13'),
('Computer Science and Engineering', 'Professor', '405G', 'AB13');

-- --------------------------------------------------------

--
-- Table structure for table `G4_warden`
--

CREATE TABLE `G4_warden` (
  `warden_id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `G5_guesthouses`
--

CREATE TABLE `G5_guesthouses` (
  `guesthouse_name` varchar(30) NOT NULL,
  `total_rooms` int NOT NULL,
  `location` varchar(100) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `G6_notifications`
--

CREATE TABLE `G6_notifications` (
  `Notification_ID` int NOT NULL,
  `Student_ID` int NOT NULL,
  `Message` text NOT NULL,
  `Sent_At` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `G6_notifications`
--

INSERT INTO `G6_notifications` (`Notification_ID`, `Student_ID`, `Message`, `Sent_At`) VALUES
(1, 2157, 'Your maintenance request has been submitted successfully.', '2025-04-15 21:03:16'),
(2, 2157, 'Your maintenance request has been submitted successfully.', '2025-04-15 21:45:20'),
(3, 2157, 'Your maintenance request has been submitted successfully.', '2025-04-15 21:53:34'),
(4, 2157, 'Your maintenance request has been submitted successfully.', '2025-04-15 22:56:30');

-- --------------------------------------------------------

--
-- Table structure for table `G7_placement_statistics`
--

CREATE TABLE `G7_placement_statistics` (
  `department` varchar(50) NOT NULL,
  `total_students` int NOT NULL,
  `placed_students` int NOT NULL,
  `highest_package` decimal(10,2) NOT NULL,
  `average_package` decimal(10,2) NOT NULL,
  `placement_rate` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `G7_placement_statistics`
--

INSERT INTO `G7_placement_statistics` (`department`, `total_students`, `placed_students`, `highest_package`, `average_package`, `placement_rate`) VALUES
('Aerospace', 2, 1, '215000.00', '215000.00', '50.00'),
('BioTech', 2, 2, '205000.00', '195000.00', '100.00'),
('CE', 4, 0, '0.00', '0.00', '0.00'),
('Chemical', 2, 1, '195000.00', '195000.00', '50.00'),
('CSE', 4, 2, '250000.00', '125000.00', '25.00'),
('ECE', 4, 1, '270000.00', '270000.00', '25.00'),
('EE', 4, 1, '195000.00', '195000.00', '25.00'),
('Mathematics', 2, 1, '240000.00', '217500.00', '100.00'),
('ME', 4, 1, '200000.00', '200000.00', '25.00'),
('Physics', 2, 1, '210000.00', '210000.00', '50.00');

-- --------------------------------------------------------

--
-- Table structure for table `G8_DIGITAL_BOOKS`
--

CREATE TABLE `G8_DIGITAL_BOOKS` (
  `Digital_ID` int NOT NULL,
  `Digital_Name` varchar(100) NOT NULL,
  `DigitalID_Book_Author` varchar(100) NOT NULL,
  `Digital_Downloads` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `G9_pdfdocument`
--

CREATE TABLE `G9_pdfdocument` (
  `DocumentID` int NOT NULL,
  `OwnerID` int NOT NULL,
  `FilePath` text NOT NULL,
  `UploadTimestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `G10_items`
--

CREATE TABLE `G10_items` (
  `item_id` int NOT NULL,
  `item_type` enum('T-shirt','Shirt','Pants','Dress','Jacket','Other') NOT NULL,
  `item_details` varchar(200) NOT NULL,
  `Price` decimal(10,2) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `G11_payments`
--

CREATE TABLE `G11_payments` (
  `PaymentID` int NOT NULL,
  `OrderID` int NOT NULL,
  `AmountPaid` decimal(10,2) NOT NULL,
  `PaymentMethod` enum('UPI','Card','Cash') NOT NULL,
  `PaymentStatus` enum('Pending','Completed','Failed') DEFAULT 'Pending',
  `PaymentTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `G11_payments`
--

INSERT INTO `G11_payments` (`PaymentID`, `OrderID`, `AmountPaid`, `PaymentMethod`, `PaymentStatus`, `PaymentTime`) VALUES
(1, 5, '220.00', 'UPI', 'Pending', '2025-04-15 16:24:55'),
(2, 6, '440.00', 'UPI', 'Pending', '2025-04-15 16:29:35'),
(3, 7, '50.00', 'UPI', 'Pending', '2025-04-15 16:36:45'),
(4, 8, '65.00', 'UPI', 'Pending', '2025-04-15 16:37:59'),
(5, 9, '60.00', 'UPI', 'Pending', '2025-04-15 17:33:53'),
(6, 10, '35.00', 'UPI', 'Pending', '2025-04-15 17:35:35'),
(7, 11, '35.00', 'UPI', 'Pending', '2025-04-15 17:41:07'),
(8, 12, '50.00', 'UPI', 'Pending', '2025-04-15 18:21:46'),
(9, 13, '85.00', 'UPI', 'Pending', '2025-04-15 18:35:49'),
(10, 14, '420.00', 'UPI', 'Pending', '2025-04-15 22:35:08'),
(11, 15, '240.00', 'UPI', 'Pending', '2025-04-15 22:38:37'),
(12, 16, '150.00', 'UPI', 'Pending', '2025-04-15 22:39:52'),
(13, 17, '5.00', 'UPI', 'Pending', '2025-04-16 04:08:01'),
(14, 18, '250.00', 'UPI', 'Pending', '2025-04-16 04:44:49'),
(15, 19, '250.00', 'UPI', 'Pending', '2025-04-16 04:44:51'),
(16, 20, '100.00', 'UPI', 'Pending', '2025-04-16 04:45:53'),
(17, 21, '70.00', 'UPI', 'Pending', '2025-04-16 04:49:07'),
(18, 22, '30.00', 'UPI', 'Failed', '2025-04-16 04:55:15'),
(19, 23, '120.00', 'UPI', 'Pending', '2025-04-16 05:11:57'),
(20, 24, '40.00', 'UPI', 'Pending', '2025-04-16 05:19:53'),
(21, 25, '30.00', 'UPI', 'Pending', '2025-04-16 05:28:04'),
(22, 26, '120.00', 'UPI', 'Pending', '2025-04-16 06:53:08'),
(23, 27, '190.00', 'UPI', 'Completed', '2025-04-16 07:01:25'),
(24, 28, '170.00', 'UPI', 'Pending', '2025-04-16 07:01:29'),
(25, 29, '190.00', 'UPI', 'Completed', '2025-04-16 07:07:29'),
(26, 30, '170.00', 'UPI', 'Pending', '2025-04-16 07:07:34');

-- --------------------------------------------------------

--
-- Table structure for table `G12_Doctors`
--

CREATE TABLE `G12_Doctors` (
  `DoctorID` int NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Specialization` varchar(100) NOT NULL,
  `Image` longblob,
  `ContactNumber` varchar(15) NOT NULL,
  `Email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `G12_Doctors`
--

INSERT INTO `G12_Doctors` (`DoctorID`, `Name`, `Specialization`, `Image`, `ContactNumber`, `Email`) VALUES
(1, 'Dr. Aditya Sharma', 'General Physician', NULL, '9876543201', 'aditya.sharma@example.com'),
(2, 'Dr. Nandini Verma', 'Orthopedic', NULL, '8765432190', 'nandini.verma@example.com'),
(3, 'Dr. Suresh Patel', 'Neurologist', NULL, '7654321098', 'suresh.patel@example.com'),
(4, 'Dr. Kavita Gupta', 'Cardiologist', NULL, '6543210987', 'kavita.gupta@example.com'),
(5, 'Dr. Rajiv Kumar', 'Dermatologist', NULL, '5432109876', 'rajiv.kumar@example.com'),
(6, 'Dr. Meera Joshi', 'Pediatrician', NULL, '9988776655', 'meera.joshi@example.com'),
(7, 'Dr. Sanjay Mehta', 'Ophthalmologist', NULL, '8877665544', 'sanjay.mehta@example.com'),
(8, 'Dr. Priya Narayanan', 'Gynecologist', NULL, '7766554433', 'priya.narayanan@example.com'),
(9, 'Dr. Vikram Singh', 'Psychiatrist', NULL, '6655443322', 'vikram.singh@example.com'),
(10, 'Dr. Ananya Desai', 'ENT Specialist', NULL, '5544332211', 'ananya.desai@example.com'),
(11, 'Dr. Rohan Malhotra', 'Dentist', NULL, '4433221100', 'rohan.malhotra@example.com'),
(12, 'Dr. Leela Krishnan', 'Pulmonologist', NULL, '3322110099', 'leela.krishnan@example.com'),
(13, 'Dr. Arjun Kapoor', 'Urologist', NULL, '2211009988', 'arjun.kapoor@example.com'),
(14, 'Dr. Pooja Sharma', 'Nutritionist', NULL, '1100998877', 'pooja.sharma@example.com'),
(15, 'Dr. Karthik Iyer', 'Rheumatologist', NULL, '0099887766', 'karthik.iyer@example.com');

-- --------------------------------------------------------

--
-- Table structure for table `G13_Route`
--

CREATE TABLE `G13_Route` (
  `RouteID` int NOT NULL,
  `StartLocation` varchar(255) NOT NULL,
  `EndLocation` varchar(255) NOT NULL,
  `IntermediateLocations` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `G14_revenue`
--

CREATE TABLE `G14_revenue` (
  `Month` date NOT NULL,
  `Payment` decimal(10,2) NOT NULL,
  `Inventory` decimal(10,2) NOT NULL,
  `Salary` decimal(10,2) NOT NULL,
  `Utilities` decimal(10,2) NOT NULL,
  `TotalExpense` decimal(10,2) GENERATED ALWAYS AS (((`Inventory` + `Salary`) + `Utilities`)) STORED,
  `TotalRevenue` decimal(10,2) GENERATED ALWAYS AS ((`Payment` - `TotalExpense`)) STORED
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `G14_revenue`
--

INSERT INTO `G14_revenue` (`Month`, `Payment`, `Inventory`, `Salary`, `Utilities`) VALUES
('2025-04-01', '60120.50', '35860.00', '3500.00', '16400.00');

-- --------------------------------------------------------

--
-- Table structure for table `G15_alerts`
--

CREATE TABLE `G15_alerts` (
  `alert_id` int NOT NULL,
  `description` text NOT NULL,
  `alert_time` datetime NOT NULL,
  `resolved` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `G16_scholarship`
--

CREATE TABLE `G16_scholarship` (
  `Funding_ID` varchar(10) NOT NULL,
  `Funding_Name` varchar(255) DEFAULT NULL,
  `Type` enum('Scholarship','Stipend','Financial Aid') NOT NULL,
  `Total_Amt` decimal(12,2) NOT NULL,
  `Allocated_Amt` decimal(12,2) DEFAULT '0.00',
  `Deadline` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `G17_customer`
--

CREATE TABLE `G17_customer` (
  `customer_id` varchar(12) NOT NULL,
  `name` varchar(255) NOT NULL,
  `contact` varchar(15) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `G17_customer`
--

INSERT INTO `G17_customer` (`customer_id`, `name`, `contact`, `email`) VALUES
('CS2386', 'asd', 'asd', 'asd'),
('CS6109876543', 'Priyanka Das', '6109876543', 'priyanka.das@email.com'),
('CS6543210987', 'Neha Arora', '6543210987', 'neha.arora@email.com'),
('CS6765432109', 'Aarti Reddy', '6765432109', 'aarti.reddy@email.com'),
('CS7210987654', 'Amit Singh', '7210987654', 'amit.singh@email.com'),
('CS7654321098', 'Vikas Patel', '7654321098', 'vikas.patel@email.com'),
('CS7876543210', 'Raj Malhotra', '7876543210', 'raj.malhotra@email.com'),
('CS8321098765', 'Sonal Roy', '8321098765', 'sonal.roy@email.com'),
('CS8765432109', 'Ananya Verma', '8765432109', 'ananya.verma@email.com'),
('CS8952343210', 'Amar Singh', '8952343210', 'singh.amar@iitgn.ac.in'),
('CS8952349087', 'Jay Kumar', '8952349087', 'kumar.jay@iitgn.ac.in'),
('CS8956543210', 'Arun Seth', '8956543210', 'seth.arun@iitgn.ac.in'),
('CS8987654321', 'Kiran Joshi', '8987654321', 'kiran.joshi@email.com'),
('CS9098765432', 'Mohan Nair', '9098765432', 'mohan.nair@email.com'),
('CS9432109876', 'Rohan Mehta', '9432109876', 'rohan.mehta@email.com'),
('CS9876543210', 'Ramesh Sharma', '9876543210', 'ramesh.sharma@email.com');

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE `images` (
  `MemberID` int NOT NULL,
  `ImagePath` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`MemberID`, `ImagePath`) VALUES
(112, 'https://www.google.com/imgres?q=icecream&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F2%2F2e%2FIce_cream_with_whipped_cream%252C_chocolate_syrup%252C_and_a_wafer_%2528cropped%2529.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FIce_cream&docid=1-Z6qSvqs3M01M&tbnid=JIPNqve6HowBHM&vet=12ahUKEwiuypiA7NSMAxUJyDgGHVuxB3kQM3oECBUQAA..i&w=2403&h=3147&hcb=2&ved=2ahUKEwiuypiA7NSMAxUJyDgGHVuxB3kQM3oECBUQAA'),
(164, 'hiiiiiiii'),
(2019, 'C://Users/Konain/Checkinout/static/images/mxphgllces.jpg'),
(2021, 'C://Users/Konain/Checkinout/static/images/kartikpillai.jpg'),
(2017, 'https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg'),
(2065, 'C://Users/Konain/Checkinout/static/images/vibhajoshi.jpg'),
(2072, 'C://Users/Konain/Checkinout/static/images/chandanrana.jpg'),
(2088, 'C://Users/Konain/Checkinout/static/images/mohitbhattacharya.jpg'),
(2089, 'C://Users/Konain/Checkinout/static/images/sunilrawat.jpg'),
(2093, 'C://Users/Konain/Checkinout/static/images/dhruvgill.jpg'),
(2097, 'C://Users/Konain/Checkinout/static/images/shilpapatel.jpg'),
(2100, 'C://Users/Konain/Checkinout/static/images/rameshvaidya.jpg'),
(2106, 'C://Users/Konain/Checkinout/static/images/namitavarma.jpg'),
(2114, 'C://Users/Konain/Checkinout/static/images/rekhabhattacharya.jpg'),
(2118, 'C://Users/Konain/Checkinout/static/images/shivanikapoor.jpg'),
(2162, 'C://Users/Konain/Checkinout/static/images/saritaphadke.jpg'),
(2095, 'static/uploads/profile_images/2095_1744724192_wallpaperflare.com_wallpaper (1).jpg'),
(2163, 'static/uploads/profile_images/2163_1744742116_GOW 3.jpg'),
(2200, 'static/uploads/profile_images/2200_1744724579_GOW 2.jpg'),
(2266, 'C://Users/Konain/Checkinout/static/images/seemaupadhyay.jpg'),
(2267, 'C://Users/Konain/Checkinout/static/images/kunaldevgan.jpg'),
(2268, 'C://Users/Konain/Checkinout/static/images/sumitvij.jpg'),
(2236, 'https://drive.google.com/file/d/14_EmDfg22gAcnRdY6aPEjIKAx712BnY_/view?usp=sharing'),
(2241, 'https://drive.google.com/file/d/1km10Sbh5-JdvJazk_ieh3n43BQ0fMsPn/view?usp=sharing'),
(24210209, 'C://Users/Konain/Checkinout/static/images/karanmehra.jpg'),
(2241, 'https://drive.google.com/file/d/1rpirdQlishEutmP5iJebSKvzzA321eZS/view?usp=sharing'),
(24210151, 'https://drive.google.com/file/d/1rpirdQlishEutmP5iJebSKvzzA321eZS/view?usp=sharing');

-- --------------------------------------------------------

--
-- Table structure for table `Login`
--

CREATE TABLE `Login` (
  `MemberID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Password` varchar(200) NOT NULL,
  `Session` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Expiry` int DEFAULT NULL,
  `Role` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Login`
--

INSERT INTO `Login` (`MemberID`, `Password`, `Session`, `Expiry`, `Role`) VALUES
('1', 'Nandu@123', NULL, NULL, 'admin'),
('10', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('1111', 'default123', NULL, NULL, 'member'),
('1112', '$2b$05$0/Y0IziIO8NwV4vfc4sYsuBE/GfmILZ/UDz8pIJb/NaV1Zt5SDZ7y', NULL, NULL, 'user'),
('1114', 'da9970210765ec26cdc2c851f8bdfadffe9dde58cfe7fc84164c493564aa8248', '86QIaKSTZFXFEeRDtSE6jzeeHdVdfVW6', 9826478, 'Student'),
('1118', '1aabac6d068eef6a7bad3fdf50a05cc8', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjExMTgiLCJSb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDU2ODQ2MH0.4_cQVMPI8bDCkjsPDCvhBvgrQY9u6APxFzEjO6vDYZ4', 1744548660, 'student'),
('112', 'default123', '78e5b74c-874a-4264-91c2-6af8e1330e9d', 1744548960, 'member'),
('1122', '482c811da5d5b4bc6d497ffa98491e38', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibmV3X3Rlc3RfdXNlciIsInJvbGUiOiJtZW1iZXIiLCJleHAiOjE3NDQ1ODY1MjAsImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjoxMTIyfQ.rQNDMtEbBSJiN-2vYyvurchEPBxC_R_iYCXYkB2QC9g', 1744566721, 'member'),
('1123', '482c811da5d5b4bc6d497ffa98491e38', NULL, NULL, 'member'),
('1129', 'default123', NULL, NULL, 'member'),
('1130', 'default123', NULL, NULL, 'member'),
('1134', 'scrypt:32768:8:1$CLvHbJMIuvo7X83T$289f75ce7752391f4d7ab875b21c6180973a59a509e4a4cfbfb7c34c7aea162aaab4b2ae86328f58387fcae5e489007da459c8169d435d7b48b987866f665c94', NULL, NULL, 'user'),
('1135', 'scrypt:32768:8:1$m1DcMZsrPQ4aCWIg$f5e1b806c3bb724cf934da1cb5b0059e5e978240bfb529236f867dbe3ba73e283d24e13a8d6e0750ffa1f636a030643f6dd69e9c7b8694f21db6bcbe5cb2c672', NULL, NULL, 'user'),
('1137', 'XiLV9wEWdi', NULL, NULL, 'user'),
('1139', '69fb127376c7bcd05caee9bed739c23f', NULL, NULL, 'student'),
('1142', '69fb127376c7bcd05caee9bed739c23f', NULL, NULL, 'student'),
('1143', 'scrypt:32768:8:1$nX1LkL3CkIWD4DJ3$351a670c9b0ac21e3d224d150d0c230f74c42284b82c4b1aa9fb03153e982855a18cffb801075bf310053875c95a7bcb96c6d25b69ff627db1b107080c15ebd6', NULL, NULL, 'admin'),
('1145', '69fb127376c7bcd05caee9bed739c23f', NULL, NULL, 'student'),
('1148', '69fb127376c7bcd05caee9bed739c23f', NULL, NULL, 'student'),
('1150', '69fb127376c7bcd05caee9bed739c23f', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjExNTAiLCJSb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDU3NjUwM30.3RouzqfFYRCokTEulmREzbqDT5kgj19G9BWOG1gG9dc', 1744556703, 'student'),
('1151', 'scrypt:32768:8:1$0TXHyIYc5WRtdZ8Y$f389155848f452a230619733778e210d81c30d94cd902eaafda35cf5bc13e1982cd1f6df9c809b60ec63e0a61bde857cc37b33034183eee530694a9efa919207', NULL, NULL, 'user'),
('1152', 'scrypt:32768:8:1$BfBivlf6BFcbRAiq$8d3b693b83b9ac85da5dcfccfa7cda80a58cc51983bfc057174741c01f5c03b54af955ce1fbe7d74ad442dd487e0f0dd91ca742ccaec2065cd2c2d31c62b6d7c', NULL, NULL, 'user'),
('1153', 'default123', NULL, NULL, 'member'),
('1154', 'scrypt:32768:8:1$222GMh5c0QvpaDB9$a67a12a29f3e6e6647912e9d70d550ae5b5c21fcc1d45c39e784b1c179dc13b97faed7f16995f905937959a7da5cbcb8fe4060b951ada86de4ad6ab304c617f5', NULL, NULL, 'user'),
('1157', 'd41d8cd98f00b204e9800998ecf8427e', NULL, NULL, 'member'),
('1158', 'd41d8cd98f00b204e9800998ecf8427e', NULL, NULL, 'member'),
('1159', '9ae8d3b4d7eddc0efe4adc6ca3c480b4', NULL, NULL, 'visitor'),
('1161', '3a294a450337f39378d0a6e548412492', NULL, NULL, 'member'),
('1162', '3a294a450337f39378d0a6e548412492', NULL, NULL, 'member'),
('1163', 'wq4wqer', NULL, NULL, 'member'),
('1165', '9ae8d3b4d7eddc0efe4adc6ca3c480b4', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjExNjUiLCJSb2xlIjoidmlzaXRvciIsImV4cCI6MTc0NDU3OTEwOH0.mnOmM-YN-0pGJ-dKQxkoAIPuFnCp2qVVs1RR21Cty3k', 1744559308, 'visitor'),
('1166', 'd41d8cd98f00b204e9800998ecf8427e', NULL, NULL, 'member'),
('1167', 'e2fc714c4727ee9395f324cd2e7f331f', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSml5YWEiLCJyb2xlIjoibWVtYmVyIiwiZXhwIjoxNzQ0NTgwNTA5LCJncm91cCI6IjEiLCJzZXNzaW9uX2lkIjoxMTY3fQ.lHTUFWN5IU7WnYuBcBcSqGhEif5-Ro4REPV7tooxrDM', 1744560709, 'member'),
('1168', 'ae95c8d644244cb39595c920c4e89bfe', NULL, NULL, 'visitor'),
('1170', '0ea11d2b39a5ebe46e1d5c126d5fb8ba', NULL, NULL, 'visitor'),
('1174', 'defaultPassword', NULL, NULL, 'user'),
('1175', 'e16b2ab8d12314bf4efbd6203906ea6c', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdHVzZXIiLCJyb2xlIjoidXNlciIsImV4cCI6MTc0NDU4MzIwNSwiZ3JvdXAiOiJ0ZXN0Z3JvdXAiLCJzZXNzaW9uX2lkIjoxMTc1fQ.bK-dZKuY8Gj2JuhdoE04GFSqaxaGzjFzvX2qg8RHx98', 1744563406, 'user'),
('1176', '0e7517141fb53f21ee439b355b5a1d0a', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMTc2LCJyb2xlIjoiQWRtaW4iLCJleHAiOjE3NDQ4NDEyOTN9.MqYgoVl6CEv4BCVG1mWjrDE53T1mOKqw7PprFKRTAHs', 1744841293, 'Admin'),
('1177', 'ad6a280417a0f533d8b670c61667e1a0', NULL, NULL, 'Student'),
('1178', '482c811da5d5b4bc6d497ffa98491e38', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibmV3X3VzZXIiLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NDQ2NDM2NTgsImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjoxMTc4fQ.iYBbexlxrF-5NDI6Lm4GSUwtH6dF_zvNhXkAlS7jzkU', 1744623858, 'admin'),
('1182', 'welcome123', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSGFyc2hpdGgiLCJyb2xlIjoidXNlciIsImV4cCI6MTc0NDc4MzEzMSwiZ3JvdXAiOjEyLCJzZXNzaW9uX2lkIjoiMTE4MiJ9.bO-RVZDRT0riIUnrCco_oq5JdhI8xsGzzB9B1hbj3vQ', 1744783131, 'user'),
('1185', 'e395ad52224de3d5e7fe38f3cb805946f6272758d572fe8a2190fa11951fcbab', '043dc713-3bfe-4e40-9c45-f7d040fc1534', 1744718485, 'user'),
('1191', 'scrypt:32768:8:1$CxijX5NwLJJEn6fM$a2f774ce38832e827bf0c76705b44a5a5d3f42c46b96d13b2bbaad39269ea11aa87cf9ec6467dbf114ff6365022a3f64c883bcaac00d77da0d722ea90130a660', NULL, NULL, 'Student'),
('1196', '2d4f343fb2bc5702c6b1a1965f6ea5fc', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTE5NiIsImV4cCI6MTc0NDU4NjkwN30.YUo-ns-riIKQ6C8769Hn90Oo3urcZ1bP4BTofS21UCw', 1744567108, 'member'),
('1197', '2c68e1d50809e4ae357bcffe1fc99d2a', 'asdf', 1744568898, 'admin'),
('1198', '1a1dc91c907325c69271ddf0c944bc72', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTE5OCIsImV4cCI6MTc0NDU5MjQwM30.Rh31ucgRE_eiAEjMrID1jSEskVIBe3uNcbT0sEdId64', 1744572604, 'admin'),
('1200', '1a1dc91c907325c69271ddf0c944bc72', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTIwMCIsImV4cCI6MTc0NDU5Mjc3N30.J35FSWjNujXIRox-1znD-VAWw2M-sNz9NUE4zyP98_A', 1744572977, 'member'),
('1214', '1a1dc91c907325c69271ddf0c944bc72', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTIxNCIsImV4cCI6MTc0NDU5NjU4OH0.lJkLS72ex_HB5Rie9ZfzbZzpxIn4uD1G5kAsHqHkBC4', 1744576789, 'admin'),
('1222', '1a1dc91c907325c69271ddf0c944bc72', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTIyMiIsImV4cCI6MTc0NDYwMzE1NX0.t43ZNXUwxJh4ACRDTOZ1Pvk_xvPJXEjQG6T3L75tcBU', 1744583356, 'admin'),
('1224', 'defaultPassword', NULL, NULL, 'user'),
('1228', '482c811da5d5b4bc6d497ffa98491e38', NULL, NULL, 'user'),
('1230', '482c811da5d5b4bc6d497ffa98491e38', NULL, NULL, 'user'),
('1232', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('1239', '1234', NULL, NULL, 'User'),
('1244', '1234', NULL, NULL, 'User'),
('1248', '1234', NULL, NULL, 'User'),
('1249', '1234', NULL, NULL, 'User'),
('1250', '1234', NULL, NULL, 'User'),
('1251', 'scrypt:32768:8:1$UDfK7oVAxYEC2m66$751980a04f114c28a9fc538a048c700593c9de5393aaa199d64a6b3e1cf79aa964134781f7d24b67281dd584b07eb679f70dd3b64f9245d5f5657b9e10883115', NULL, NULL, 'user'),
('1252', 'scrypt:32768:8:1$qlHcBYsG1G5K5k64$cab4680ff924d920c6c42291906f6b6bef72a8fa8d28e54d4bb2dc3016228f6ed13d499930ddae2d4157ea6ed7f30a392a12d00d834c3622c727e035552391b8', NULL, NULL, 'user'),
('1253', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('1256', 'admin123', NULL, NULL, 'admin'),
('1257', 'scrypt:32768:8:1$tfDTptyAjOfvwBK5$edfd6aedc513c081d29b955552ba02e327c23aef4707939e5ff5b60bed2099a9768243b5d2cd4041d2e381ae3f63da5a9d58b4ca286c1c34f4fd07918928836c', NULL, NULL, 'user'),
('1258', 'scrypt:32768:8:1$51y7Cb1Oh60kykMU$daa90891f428b26b43d805f6a52d04369f4ea5fd65e803e497383ea8a177bcb7f5a7a8064749e39197ea10c78c621ae77ad462c27cd3e8adbb32db84ced90cfa', '7bacd8c5-dec8-4898-9e1b-21fe62620a90', 1744638001, 'user'),
('1259', '$2b$05$C5kFT97/WU4VkE5cDhFHkOK3rq.4QOQYP.2CiN8Fkr0/5J8vmmk8O', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTI1OSwidXNlcm5hbWUiOiJuaXNoaXRfY2giLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2MjAzODgsImV4cCI6MTc0NDYyNzU4OH0.5dA31x5PA7rU8TCwcO2A05c5_eKuZbDF6Apu8pSV0Wg', 1744627588, 'admin'),
('1262', '$2b$05$Dmrf0F5FghG00Swpsaz1M..tfZV9ylgA6m2fSREPdlCEiNtNcXNnS', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTI2MiwidXNlcm5hbWUiOiJuaXNoaXRfY2twIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzQ0NjIwOTk3LCJleHAiOjE3NDQ2MjgxOTd9.KfYG0NTmGOoheuBwJZFrbKL5vCKCnIsr2kYDK3SY2uA', 1744628197, 'admin'),
('127', 'default123', '3f69dde2-4c02-4fd3-baf0-cd3c8d40eb4b', 1744629786, 'member'),
('1300', 'admin123', NULL, NULL, 'admin'),
('1301', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('1302', '1234', NULL, NULL, 'User'),
('1303', 'b59c67bf196a4758191e42f76670ceba', NULL, NULL, 'visitor'),
('1304', '$2b$05$rF5J5RRYdJdG/z8xLPc3kOLoRZW4VmySGHrvLJORkMH9rv9kSLaMy', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTMwNCwidXNlcm5hbWUiOiJuaXNoaXRfY2tucCIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYyMTQ5OCwiZXhwIjoxNzQ0NjI4Njk4fQ.Xl53sM1YjEwZYb-rSGXy9048Vc4gLYNWM1BRRDxLuNY', 1744628698, 'admin'),
('1305', '0d2ba14252e0a370462444fef3df28cb', NULL, NULL, 'student'),
('1307', '0d2ba14252e0a370462444fef3df28cb', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjEzMDciLCJSb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDYyNjkyMn0.nv7tx3Tyq0RK5zlrSorx2IMBeOaq46nqF1GsWngXYow', 1744607122, 'student'),
('1309', '$2b$05$SUggUMGfXlEd01dJ0lz92e1i7vmodEKP6kLr52Y85uoj8D5pYGxMO', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjEzMDkiLCJ1c2VybmFtZSI6Im5pc2hpdF9ja25wbWgiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2MjMwMzUsImV4cCI6MTc0NDYyNjYzNX0.FeAS_GJP5ETJHFaJe_pacJtf1tCzURAExl8eE-H7CwA', 1744626635, 'admin'),
('1310', 'scrypt:32768:8:1$t687fgjedz2unrdj$40ec5018e670d81bb19e68b67ed087ce6cda175be089b7ee806f36503c5c4ff71f8ab2f8f36a07be0e7e8c519ad89f97852f28902b503d7da37ca1d06e4a7afa', '29de0b98-363d-4f4c-b30e-0ef28bc39000', 1744790974, 'user'),
('1311', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('1312', '$2b$10$0vKsFeiNsB8o8iwo1rbmAucBjjqb/teGmPt/NFekv0RU8V5AjQD8i', NULL, NULL, 'user'),
('1400', 'admin123', '8aa70ca4-b6d2-4bba-a7f3-875397fa7693', 1744639155, 'admin'),
('1402', '1234', NULL, NULL, 'admin'),
('1407', '$2b$10$/2bfOmC7EGD.ZnC0fL05LeNcjAT2g50K9MDHhN8RDgEI5sKcwFiJO', NULL, NULL, 'user'),
('1408', '3dc1e4c3bc5b2ae63520627ea44df7fd', NULL, NULL, 'student'),
('1411', '$2b$10$hUZ39FsgnZYhFQYkSxYK/u0h4zXSw4WASWQKkPIKzWV075OOwTnjS', NULL, NULL, 'user'),
('1413', '$2b$10$rc0H0wdJFfVhNxsB6V3gDuxTWhzvR1VATfUGG4Udj1c4UIz1tg9i2', NULL, NULL, 'user'),
('1414', 'admin@123', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxNDE0Iiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzQ0Nzg1MTgxLCJleHAiOjE3NDQ3ODg3ODF9.ODKnhFzVVUwW_c-dLTGq16soRnoyHwJcJVhi-9qg6VU', 1744788781, 'admin'),
('1415', '1234', NULL, NULL, 'admin'),
('1417', '3dc1e4c3bc5b2ae63520627ea44df7fd', NULL, NULL, 'student'),
('1418', '3dc1e4c3bc5b2ae63520627ea44df7fd', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjE0MTgiLCJSb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDYyOTc4MH0.REz16hg3fw-SXBDzNQQfZp0YHm70UrtpzceQEiO--_E', 1744609980, 'student'),
('1419', 'pbkdf2:sha256:260000$R8MKwfCl3L4aK15C$1f52fe44cec650bb7a6eba7fa927fa9f129d33c2fae4dabeb110068349a7f7e7', '68c911e7-fc7c-4f76-a51f-ce672fb3f527', 1744633814, 'user'),
('1428', 'default123', NULL, NULL, 'member'),
('1430', '$2b$05$DeloX1sX6nFPmwn0zG.MUefr13k4ipEloafhwkaL.b4pOq4Zs7Gxq', NULL, NULL, 'user'),
('1435', 'pbkdf2:sha256:260000$BtW3O6JFjove2m5t$b09bb35627c6e4b51f61c2e3490e066b702704f24f0be9594945e15035420b9a', 'c4ecc29a-7f1c-4701-8e39-6c6b39aeaac1', 1744631807, 'user'),
('149', 'admin123', 'c807721b-e8b0-466b-af8d-27c7329a7442', 1744392573, 'admin'),
('150', 'default123', NULL, NULL, 'admin'),
('16', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('160', 'default123', 'c5949095-4d6c-4f02-a1bc-424d035f2e2e', 1744709508, 'member'),
('164', 'default123', NULL, NULL, 'member'),
('18', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('19', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('192', 'default123', 'bf4614bf-6447-49c2-9662-a78eacc95c2a', 1744725917, 'member'),
('20', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('2001', 'password123', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0NDciLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2MzY3MTQsImV4cCI6MTc0NDY0MDMxNH0.j57z4Ktjq_r4jYqKCF_dB8xarsNeOgxKszG7E5OKe3I', 10800, 'admin'),
('2002', 'password456', NULL, NULL, 'Coach'),
('2003', 'password789', NULL, NULL, 'Player'),
('2004', 'password101', NULL, NULL, 'Organizer'),
('2005', 'password112', NULL, NULL, 'Referee'),
('2006', 'password131', NULL, NULL, 'EqManager'),
('2007', 'password415', NULL, NULL, 'Player'),
('2008', 'password161', NULL, NULL, 'Coach'),
('2009', 'password718', NULL, NULL, 'admin'),
('2010', 'password192', NULL, NULL, 'Referee'),
('2011', '9LqzUE9rmT', NULL, NULL, 'user'),
('2014', '482c811da5d5b4bc6d497ffa98491e38', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMDE0LCJyb2xlIjoiQ291bmNpbCIsImV4cCI6MTc0NDY5ODI4Mn0.xzyAm-8kKZ26RMY6nIB8u8yGoI3ricRPaWjZh2C1bDQ', 1744698282, 'Council'),
('2016', 'pbkdf2:sha256:260000$PJ2LwYsZOwb0rrdb$54cab655e951f820b146f2e7ac1282d0b417773a6df64f6dfe17472361310e90', 'SHZOW_AukNZhfkuq_g_4w6yryPLFbfA2Kz3HI2CK-yo', 1744652672, 'user'),
('2017', 'youup', '09a00355979cba70828e29844a70e77a0651abaa40f1c44ab24b1164c7e2a10c', 1744779406, 'admin'),
('2018', '1234', NULL, NULL, 'User'),
('2019', '52d9df25355b7a1531231bc7351e3a1bf20dc0950e8777d2c5186fecd264fccf', 'CDpTbeBIiXc2dq5mSQXTSX3Pax57UIiF', 7109830, 'Student'),
('2021', '88e26a1865f1b6cb382f8ebfae8a69da33dc3cfe72bdd28c8c74fcbf50c43fe6', 'GPKYEl97XBlMoac2LWc8UtsnkxV04YdG', 6321797, 'Staff'),
('2022', '934b535800b1cba8f96a5d72f72f1611', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIwMjIiLCJSb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDYzMTE3OH0.5nQGGo3_okxrbtqAERn_x-AE0k9ycgELXvfdLUN3LaA', 1744611378, 'student'),
('2023', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2024', '934b535800b1cba8f96a5d72f72f1611', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIwMjQiLCJSb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDYzMTI5MX0.ltY75H2hICm7_5scnusrZqeReOJhtq6N7kdJ9b65B3g', 1744611491, 'student'),
('2025', '$2b$05$Zm4SZV4T10jVm0eZ2.YcS.vpC0t2fzcK2lzQLgN5rJdOyctf9czJC', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjAyNSwidXNlcm5hbWUiOiJuaXNoaXRfY2tucG1oMiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYyNzc2OCwiZXhwIjoxNzQ0NjM0OTY4fQ.O_2B_SydTCe6kjZ6dhD7f0HR_GnaTp6P8Vb5CqKhxes', 1744634968, 'admin'),
('2026', 'd84d34224176f0f54b8abd65f639a547', NULL, NULL, 'user'),
('2027', '5b3ce5529c9b0133387e9a7918d79ce88ae7e9d295fd1620248df3a4471b6101', NULL, NULL, 'user'),
('2028', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2029', 'admin@123', NULL, NULL, 'admin'),
('2030', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2035', '1a1dc91c907325c69271ddf0c944bc72', NULL, NULL, 'member'),
('2037', '1f5388dc33dd51dfcd22a738735270908dde00dadbb6d0db4f5e2dbe38f4e98e', '5790a20d-6548-46aa-b696-8d4b4fa3536e', 1744719216, 'user'),
('2038', 'e754546f365c419e8ff7f2d588013ea3', NULL, NULL, 'member'),
('2040', 'd84d34224176f0f54b8abd65f639a547', NULL, NULL, 'user'),
('2046', '3dc1e4c3bc5b2ae63520627ea44df7fd', NULL, NULL, 'visitor'),
('2048', '3dc1e4c3bc5b2ae63520627ea44df7fd', NULL, NULL, 'visitor'),
('2049', 'scrypt:32768:8:1$eikZPB2ilnCms1Zv$321de5fd14a4ab8723ed385962b2bad06e99a03192dd432b4efa0859ba8049975248a4429acb4a6f0a5646f92c894e9627a8909dc65b33d5620c867ac0698376', '7ad581e0-2bb5-4001-a6b3-516406ebc646', 1744638656, 'user'),
('2050', '3dc1e4c3bc5b2ae63520627ea44df7fd', NULL, NULL, 'visitor'),
('2052', 'b59c67bf196a4758191e42f76670ceba', NULL, NULL, 'visitor'),
('2054', 'e9335e177b288c7af4af8f1225c3f938', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0NDciLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2MzEzMzQsImV4cCI6MTc0NDYzNDkzNH0.ndXYC7nRcbVQLUJI0sdfhoWocEtMyBC3nX3c8sl4W2I', 10800, 'player'),
('2056', 'scrypt:32768:8:1$wOhEoAAUVqe1SPs1$184fed1968aa4a89f35029fcb967ef75e229d123d18e71d70a89efbd80083b837323e2e5e7b93b01b017d00e22407f4bbef258052fcdd08cb402421367cf6ba4', 'd3b8c7c9-dbf2-4e89-bf46-8c3659fc458c', 1744638725, 'user'),
('2057', 'b59c67bf196a4758191e42f76670ceba', NULL, NULL, 'visitor'),
('2058', 'YWi6kiEGu6', NULL, NULL, 'user'),
('2059', 'b59c67bf196a4758191e42f76670ceba', NULL, NULL, 'visitor'),
('2061', '2be9bd7a3434f7038ca27d1918de58bd', NULL, NULL, 'visitor'),
('2062', 'scrypt:32768:8:1$ba9RhPY4GfZXFbi9$41cf463bfeab2ddb60f10ee94c246b3e7459669c4f4ac89f4309514b827a5bb16304f4f8ee1d546cdf44e833a977ac3754daa54715b4a80d13a9a521955874c7', NULL, NULL, 'user'),
('2064', '2be9bd7a3434f7038ca27d1918de58bd', NULL, NULL, 'visitor'),
('2066', '2be9bd7a3434f7038ca27d1918de58bd', NULL, NULL, 'visitor'),
('2068', '3dc1e4c3bc5b2ae63520627ea44df7fd', NULL, NULL, 'visitor'),
('2069', 'scrypt:32768:8:1$pKOAhy7FOxmmY8g2$73a907bbe35403048b085a704671b854f4a592281673a191c9addcf50fa5d5308e772a596ede36004800069fd30b0298f51db483120a813c0e1cb1da666dbf1b', NULL, NULL, 'user'),
('2070', '3dc1e4c3bc5b2ae63520627ea44df7fd', NULL, NULL, 'visitor'),
('2071', '4a7d1ed414474e4033ac29ccb8653d9b', NULL, NULL, 'visitor'),
('2072', 'dd750145d979277b95291deff96f79eec13ce5f1e85e825a4dc3afffae6710ea', 'oNVg59kmRwXLbtuEoobYJdqGn0fMV4Mq', 8966294, 'Student'),
('2073', 'b59c67bf196a4758191e42f76670ceba', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIwNzMiLCJSb2xlIjoidmlzaXRvciIsImV4cCI6MTc0NDYzNjQxN30.-Qg720NMvfJwcFSHpVVOA587i_CLIbUBo9xjRLS8SP0', 1744616617, 'visitor'),
('2074', 'b59c67bf196a4758191e42f76670ceba', NULL, NULL, 'visitor'),
('2078', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2080', 'ce5eceb14ac2bc24de2ad5f533d7d84b160714cb3bb485c94a90fc987cc88984', '5cea49df-bcf5-4054-853a-a31be3d4693f', 1744868579, 'Admin'),
('2083', 'c7d84e0c1e60ef7b3fb55fd86c1a8d0b', NULL, NULL, 'member'),
('2084', 'scrypt:32768:8:1$iSvYZn9ExWrTvC1Y$867e512a3c4d84d5ae2f61f8bfc179d901a68c5f9c150ebe5f3c3377e1076a13102b53403e857b8dcb5dc29694fc40674ed29036fe20012903ac91778d641cf0', NULL, NULL, 'user'),
('2086', '0d0fd7c6e093f7b804fa0150b875b868', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIwODYiLCJSb2xlIjoidmlzaXRvciIsImV4cCI6MTc0NDY0MDg3M30.oUk5rjqOPLdnBjDMDDo7ORP42M6ziBpNGwAwAmWgRB8', 1744621073, 'visitor'),
('2087', 'justchill', NULL, NULL, 'admin'),
('2089', 'f046b752d2d11c98dfbe1cf0b1ce15c4c1e1664aca91c3173de0ff89d4d9d8f7', 'caWavIZ1icFlMIU6qkqeHgC3Q4oNQMZS', 7066417, 'Visitor'),
('2092', '789d501ae39fde3817ba4fb0d844352e', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjA5MiIsImV4cCI6MTc0NDc4MTEwN30.VTKoZsEfyP9QD6RnS_Y7vYL5OdUosdaSY6TKJOnaeXE', 1744761308, 'member'),
('2093', '6baf36a8a335c55e8eef90a4ec964e54d9e5349ec2d6bc395ee88b73ddf05062', 'hIOb9xIkuDyPYxe8NJFSqvwF6qaN9yFk', 6940563, 'Student'),
('2094', '9a281eea0823964dfb2915823c248417', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjA5NCIsImV4cCI6MTc0NDc4MTIwNX0.dgfxrkuRiucl3GU7pd1JwH9NSvHIvzhHogyptEBkjpE', 1744761406, 'member'),
('2095', '1c0f1b3576a0a0c525e47a5b51b5723e', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZGlwZXNoIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzQ0Nzg3ODQwLCJncm91cCI6IjExIiwic2Vzc2lvbl9pZCI6MjA5NSwiaWF0IjoxNzQ0Nzg0MjQwLCJqdGkiOiJlYWRjNWZmYzg3ODFmMjYyNTUxNThkNzFjYjE1YjBkZiJ9.xLDpCx3qrtfEOHQ6PglCdODQrde3q93DB6EOJ4ld11A', 1744787840, 'admin'),
('2096', '$2b$05$spwyXWTh7VPpW4MPTrQJA.34ZJTREC1pAkXeG49cLXN4fkDBFWX0a', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjA5NiwidXNlcm5hbWUiOiJLZW5kcmljayBMYW1hciIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYzNzk0NCwiZXhwIjoxNzQ0NjQ1MTQ0fQ.skOkl6deqhiptEVx64_1DGNPoyiki-ylzakiVcJ_w40', 1744645144, 'admin'),
('2099', '$2b$05$4KNauc4/FbhBPS.4/qTHy.uzVJ/7KOFCEwfl4XKB4IgzJG2sifGC6', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjA5OSwidXNlcm5hbWUiOiJLRG90Iiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzQ0NjM4MDQ4LCJleHAiOjE3NDQ2NDUyNDh9.770-UPFYRDIBJV1VNI6NR8N7nKlVFKoRB16owijQ1ec', 1744645248, 'admin'),
('2100', '9936473fc3e4214cc50ee3fc234ba9928a2b86a8617aeeb4b70ee0b47a80b5c7', 'TX9nlCU9PHnz1acpHVrl4aIeavgMO9rZ', 8746809, 'Student'),
('2102', '$2b$05$4DRaWOHHVWV9aqv0ZKwjU.hgzg8NWPlT9XPCJjLpaeprIAyyTkLI2', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjEwMiwidXNlcm5hbWUiOiJLRG90MSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYzODI0OSwiZXhwIjoxNzQ0NjQ1NDQ5fQ.yFgWTGgDJWWq27jX_yL8BOz6yL6na-1xN0aTXUmNJ5o', 1744645449, 'admin'),
('2103', '$2b$05$1MTpxlquO5dF9NLh9ovcoeS0lXltNErwVsQNwINJVqzx1GpNuQa/q', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjEwMywidXNlcm5hbWUiOiJLZW5MYSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYzODQyMSwiZXhwIjoxNzQ0NjQ1NjIxfQ.RBFPPpaX3uVVf5LE-dY46Nk9u9wwmVbQe1YvbRj0Pr0', 1744645621, 'admin'),
('2104', '9f763f085bc07e79baaf4768979e6ee6', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjEwNCIsImV4cCI6MTc0NDYzNzA1N30.MbuqZjAzZbzcKVbz-eJOMSjZFQdh9CU4GBuEdmd49GQ', 1744617258, 'member'),
('2105', '$2b$05$Jg67do5MRVcQOuiOu4BOx.DDNj0OPOMajTD6pGNmebQI28b3joaZS', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjEwNSwidXNlcm5hbWUiOiJQZXJzb24xMiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYzODUzNSwiZXhwIjoxNzQ0NjQ1NzM1fQ.FIHZw0CX89Zj2dg_oviTdfsGJwmN1d1s00KLhTxZ_qk', 1744645735, 'admin'),
('2106', 'e97e3b29bcd31d3988ab4661902a3cc7f4e6b0d71679cb81bbe13cc167411e6f', 'CtgUjHjgyU94HSrj64vfgzTkFh76MpvL', 7682627, 'Staff'),
('2109', '808b832900747dfa6be29fe95c4a91e3', NULL, NULL, 'member'),
('2110', '3a5ba419d10b152d73e755e67246eaffd9929711f2e43bc07d37bb7fec6a9c26', NULL, NULL, 'admin'),
('2111', '99a631372a83ff261eae05acb04eb34ba05cf5d8dd3596e1648c5546c0ae18f8', NULL, NULL, 'Chef'),
('2112', '1de12e47f50f37ed7be86e8a06fb6cab', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjExMiIsImV4cCI6MTc0NDYzNzQ3NH0.HynGDH4Ibm0BxKXEWiLMa7hyCU7g_lsSfPGmx2FZnt0', 1744617674, 'member'),
('2113', '2be9bd7a3434f7038ca27d1918de58bd', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIxMTMiLCJSb2xlIjoidmlzaXRvciIsImV4cCI6MTc0NDY0MjYzN30.zEt0M2N7uKv9D2SHYCqm6aqI1elD-sOLNOfexExjcPk', 1744622837, 'visitor'),
('2115', '7d5c009e4eb8bbc78647caeca308e61b', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjExNSIsImV4cCI6MTc0NDc1NDY2Nn0.zcRakKH_Aqn36cWBtiDDlAeDAZDDK2ivF4LvfGwAvuo', 1744734867, 'member'),
('2116', '$2b$05$//UVEAnQ7ezJMyviS7vDLODqyeQeIBJsL0hRwLOhvEhe1tp2am7tC', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjExNiwidXNlcm5hbWUiOiJLZW5kcmlrTGFtYXIiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2MzkzNDAsImV4cCI6MTc0NDY0NjU0MH0.9A4l-Yq1z3Of9xUwfnizaQmLg8x4st8PodEaFRbKQYM', 1744646540, 'admin'),
('2117', 'e9335e177b288c7af4af8f1225c3f938', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0NDciLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2Mzk1NjcsImV4cCI6MTc0NDY0MzE2N30.1t1J5xo5Yjn-6k5v3AThl_69assHuY5HesPFGsqg918', 10800, 'player'),
('2118', 'b8d3c27ebc4067cedd66f9827fd0bb819e67b215ab44543e4da97f509becdda5', 'MOkSXtDiyCAl1y2hwKFkTmipTU8fsBC6', 7065719, 'Visitor'),
('2119', '6627415e807ee33c7302917216e7da68', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVlcCIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0NDY1MjM0MywiZ3JvdXAiOiIxIiwic2Vzc2lvbl9pZCI6MjExOX0.wHKSOpqrJdTrZiZtAZa1gv-JHREmcP2Nl3ykKZIKzoc', 1744632543, 'admin'),
('2120', '9f7183e53cc36671b76ae5301b69022c', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVlcC0xIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzQ0NjQ0MDkzLCJncm91cCI6bnVsbCwic2Vzc2lvbl9pZCI6MjEyMH0.mdX-a6OXfNJnneodTXFA-pdBC1ww_J9KdaeJiMlQsdA', 1744624293, 'admin'),
('2121', '449f38c05beb776f9ffffa96f423a922', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVlcC0yIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzQ0NjQ0MjY5LCJncm91cCI6bnVsbCwic2Vzc2lvbl9pZCI6MjEyMX0.utwqJ3yVb83nvEgdEJCMgvZrg-SkIHuAnSXQa0XtedM', 1744624469, 'admin'),
('2122', '006d2143154327a64d86a264aea225f3', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiVnJhaiIsInJvbGUiOiJtZW1iZXIiLCJleHAiOjE3NDQ2NjA3OTQsImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjoyMTIyfQ.cFk59IBRtrLu424u42mu2rK9QTCn3efK2VPeQYTwHb8', 1744640994, 'member'),
('2123', '1234', NULL, NULL, 'admin'),
('2124', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTI0Iiwicm9sZSI6InVzZXIiLCJpYXQiOjE3NDQ3ODUxNTAsImV4cCI6MTc0NDc4ODc1MH0.qnCzS8Rm1eVOmkLT6L_P_47G2RUbeXZVvqUdthvwU_8', 1744788750, 'user'),
('2125', 'scrypt:32768:8:1$2rFt30KGkdyokrPI$3150146136d0f04b61d9bb042702341d8f641aed529f1c519069fd3c71a4b4db330957d269b99bc34f72d9d737e3e7cd3afd448a72c4944df9172ecc6c17db6a', NULL, NULL, 'Student'),
('2126', '1234', NULL, NULL, 'admin'),
('2127', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('2128', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('2135', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('2136', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('2138', '4e65bf32d3ea9a991b5826b7ce54893f7513336d9f2e22fa1f707f3832092d54', '4EujkUuZkavjIh9ByZCJOggIYyFJH2P7', 8026956, 'Student'),
('2141', '$2b$05$P/I4VI0Nv42lMN4HW6zw6eCTOver/VCya5bMy97EomrroLmXqVRV.', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjIxNDEiLCJ1c2VybmFtZSI6Im5pc2hpdF9ja25wbWgyMyIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDcyMTk4NSwiZXhwIjoxNzQ0ODA4Mzg1fQ.wRTi25InJy_uiS95d1tNXpfbn_YZ5eID8rV_SRttvGY', 1744808385, 'admin'),
('2142', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2144', 'e9335e177b288c7af4af8f1225c3f938', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0NDciLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2NTQxMTcsImV4cCI6MTc0NDY1NzcxN30.g-5mmDF0wAnyjMJ04G1bWjcOlkHMV4VKk_w0KK8ZuTQ', 10800, 'player'),
('2145', '0d0fd7c6e093f7b804fa0150b875b868', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIxNDUiLCJSb2xlIjoidmlzaXRvciIsImV4cCI6MTc0NDY1NzkxOX0.dpMX6HF7TXzwuIUMyCfaNmPwGJdO7mr3fInH7fRPISg', 1744638119, 'visitor'),
('2148', 'f673d9991a246dbce15d315e7716bc1f', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIxNDgiLCJSb2xlIjoid2FyZGVuIiwiZXhwIjoxNzQ0NzkwMDk1fQ.Gux8Z7tPaxyiDDtBht7EZMOU29ybLgudhqs5wRhNBH0', 1744790095, 'warden'),
('2149', 'defaultPassword', NULL, NULL, 'user'),
('2150', '006d2143154327a64d86a264aea225f3', NULL, NULL, 'student'),
('2151', '006d2143154327a64d86a264aea225f3', NULL, NULL, 'technician'),
('2152', '006d2143154327a64d86a264aea225f3', NULL, NULL, 'admin'),
('2154', '006d2143154327a64d86a264aea225f3', NULL, NULL, 'student'),
('2157', '006d2143154327a64d86a264aea225f3', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiVnJhaiBTaGFoIiwicm9sZSI6InN0dWRlbnQiLCJleHAiOjE3NDQ3NzU2ODksImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjoyMTU3fQ.3gTbOBnw7z-9i-Wv_TXyJrgxP31MDCqaZ5pzXkVPthQ', 1744755890, 'student'),
('2160', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2161', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2163', 'c90a918b859bd1e56cf99af6246b128e', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiTVAiLCJyb2xlIjoidXNlciIsImV4cCI6MTc0NDc4OTk3NCwiZ3JvdXAiOiIxMSIsInNlc3Npb25faWQiOjIxNjMsImlhdCI6MTc0NDc4NjM3NCwianRpIjoiNGMyOTY4MjgwNWI1OWQ1NTFlYmRlYmNkZGY3ZGMyNGUifQ.3BaiQs0nv_wB3xAn7GZPIOzmYq346nq_4McXfVcITII', 1744789974, 'user'),
('2164', 'scrypt:32768:8:1$BbC9veLUJ5oXglBu$16f29fbfb684660bd596fe52c767429ee323240e432942b4f2c87f9fa755a45c6b5702ab4365b7f97e9e4a40ef28c0a5ea3ef87dac2ce9317422923d9d89f227', NULL, NULL, 'Student'),
('2166', 'defaultPassword', NULL, NULL, 'user'),
('2167', '6432f20f6e268d2d6cf92b51369105a9', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjE2NyIsImV4cCI6MTc0NDY2NzMwOX0.ih_Yuk_0Lf-DSbJibL_hK1U7NqRXiNVP2fhz_B1FU_U', 1744647509, 'member'),
('2168', 'scrypt:32768:8:1$wXIXZ6d3hxKCnQ5j$eb2a498506df001b898f9aa19163546009b352c7947ebe0c39eba8659fa915fdbf3c713ae41d3d25a44183e90be8beb3de12b4a28a7956f0007d31fe13c281cf', NULL, NULL, 'Student'),
('2172', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('2173', '006d2143154327a64d86a264aea225f3', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiVGVjaG5pY2lhbiIsInJvbGUiOiJ0ZWNobmljaWFuIiwiZXhwIjoxNzQ0NjkwODgzLCJncm91cCI6bnVsbCwic2Vzc2lvbl9pZCI6MjE3M30.p_mq57Eeh_-nnVbqhAFbUmcsAhHn14cTtoOben3QtJM', 1744671084, 'technician'),
('2174', '006d2143154327a64d86a264aea225f3', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiRGV3YW5zaCBTaW5naCBDaGFuZGVsIiwicm9sZSI6InN0dWRlbnQiLCJleHAiOjE3NDQ2OTEwNTMsImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjoyMTc0fQ.-rrmkTN3TXJ9ZddOCA9sTtHNQoHDW_P5hoeJ0oGED10', 1744671254, 'student'),
('2176', 'f925916e2754e5e03f75dd58a5733251', NULL, NULL, 'Student'),
('2188', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2191', 'adbf5a778175ee757c34d0eba4e932bc', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjE5MSIsImV4cCI6MTc0NDcwMzUyMX0.ZsZdvC7St6VHGiJAS6hBul9z7Let9wROWu96xz44Cy8', 1744683722, 'member'),
('2192', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'admin'),
('2193', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Organiser'),
('2197', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('2198', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('2200', 'cd203ccd68b84de1c5df8fd890e104e0', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiUEIiLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NDQ3NjIxMTksImdyb3VwIjoiMTEiLCJzZXNzaW9uX2lkIjoyMjAwLCJpYXQiOjE3NDQ3NTg1MTksImp0aSI6IjJlMzc0ZjNmMjczNGE3NzA0MjEyZjBmNjA5YTZkODA3In0.Rv2f2rthp4ROhw5MXIet1ZckJcdubA_i41sDZSuQ31k', 1744762119, 'admin'),
('2202', '09a0877d04abf8759f99adec02baf579', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjIwMiIsImV4cCI6MTc0NDcwNjk1Nn0.d6wfk6VxqrxNjOsxvdFKnzaBx5-EyhZCPPMrXtBVgTY', 1744687156, 'member'),
('2203', '698d51a19d8a121ce581499d7b701668', NULL, NULL, 'visitor'),
('2204', 'cf680ee44421c0367a36ed8ff51d25fa', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIyMDQiLCJSb2xlIjoidmlzaXRvciIsImV4cCI6MTc0NDcxMTMzOH0.YeA51OmRBMNe1mJe-yKzibkjkudAJZx1GAJOHEC7i68', 1744711338, 'visitor'),
('2205', 'scrypt:32768:8:1$vfwLcQywF4V4wmSn$e3767dbd715947ebf7e5fef89ce2b93d3787e839fea07351617b2f8145ee123a5353d261e693b100b21c8cde30678966858f8ce4f8401919de5d54bcb78e7178', NULL, NULL, 'user'),
('2208', 'e1352a3103dfa46eccd15b7530535c3d', NULL, NULL, 'student'),
('2209', 'e9335e177b288c7af4af8f1225c3f938', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMjA5Iiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzQ0NzM4MDUxLCJleHAiOjE3NDQ3NDE2NTF9.nCKjk5y9ZNy-rkz9SZZY9rdnADTJXP7-w6ttv_a-YEE', 1744741651, 'admin'),
('2210', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Coach'),
('2211', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'organiser'),
('22110206', 'admin123', NULL, NULL, 'admin'),
('2213', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Organiser'),
('2214', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Referee'),
('2215', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'EqManager'),
('2216', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2217', 'scrypt:32768:8:1$tBBGhLnwzpR9dwsb$2724c8bef8e2b5418376294fddcdd42170eb7e359d07cd342e11b056ca2d3b67f7f9965798a56d684472bc41af6bf4f9122776e433a3081057cfc01c8d784781', NULL, NULL, 'Visitor'),
('2218', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Organizer'),
('2219', '5af8aae00e4545ed0e371f90de9edf77', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjIxOSIsImV4cCI6MTc0NDczMDE0Mn0.7U9zyNaVlZ6IaFfxy2vzXttu8mW9VRs-HUkjJnzM7Ao', 1744710343, 'member'),
('2220', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Coach'),
('2221', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2222', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2223', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2224', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2225', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2226', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2227', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2228', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2229', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2230', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2231', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2232', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'Player'),
('2235', '$2b$05$G9NN4FsWSRVKXWgzDqqYSOAM4ugI1YE5LjTB8dN/w6uBNTJ9x0VNi', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjIyMzUiLCJ1c2VybmFtZSI6IkhpaWkiLCJyb2xlIjoidXNlciIsImlhdCI6MTc0NDcyOTU2OCwiZXhwIjoxNzQ0ODE1OTY4fQ.rsouv_xAzjcxDKNmPXlDmbRHR1CfiFxOUiDXgMBulok', 1744815968, 'user'),
('2236', '$2b$05$4DoLIGZ1aZN12bLE8ofKEeyGmPZPgRqJH.wbz3B/JDP.QV8bG3k5C', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjIyMzYiLCJ1c2VybmFtZSI6IkhpaWlfYWRtaW4iLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ3MzI2OTIsImV4cCI6MTc0NDgxOTA5Mn0.n6PzBaPVY8-6XQ0snP4PjohlmHINZjcQ0onlH2VpBJ8', 1744819092, 'admin'),
('2237', '2a70fb7477c294559ceb246e1109879f', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZmFyaGFuIiwicm9sZSI6IlN0dWRlbnQiLCJleHAiOjE3NDQ3MjQ4MDQsImdyb3VwIjoiMTEiLCJzZXNzaW9uX2lkIjoyMjM3LCJpYXQiOjE3NDQ3MjEyMDQsImp0aSI6IjMzODQ1NWZlMTdiMjAwYzMwODU3NjQ4MmYyZDYzMTY4In0.74zecWiFAS9sIK8EVZ_LdMGT0H9JgcEe3CiAiuLV1fA', 1744724804, 'Student'),
('2239', '3f94b481ee34e0525cfde11bdb019e7c', NULL, NULL, 'Student'),
('2241', '$2b$05$km9xeuoxOHs.MgnffhtPE.mDrz7/tLN6fY3caiaaCKkaLIkW9ioQm', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjIyNDEiLCJ1c2VybmFtZSI6IkhpaWlfdXNlciIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzQ0NzYwNzc2LCJleHAiOjE3NDQ4NDcxNzZ9.MlFhsKF5KeEHdmZvShyrvfWBTyNFz4skusdAbxoYfk8', 1744847176, 'user'),
('2242', '8e4947690532bc44a8e41e9fb365b76a', NULL, NULL, 'Student'),
('2244', '332db9c0b81c5955d194fe389698cdf8', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NDc2ODMwMCwianRpIjoiMThjNGJjNGYtMmM4ZS00MjU0LTlkOTAtN2E3NGJmMzQ2MmYxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MjI0NCwibmJmIjoxNzQ0NzY4MzAwLCJjc3JmIjoiOTFiYTg5YjUtNjJkMS00OGQzLWJmMGMtYTViZWMyODMxOWM0IiwiZXhwIjoxNzQ0ODU0NzAwLCJyb2xlIjoiQ291bmNpbCJ9.FvueRqtW3hqrpvqcjNuEoat0yUfBr3KXw1atZox0r-8', 1744854700, 'Council'),
('2245', '1a1dc91c907325c69271ddf0c944bc72', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjI0NSIsImV4cCI6MTc0NDcyNzk1OX0.9ln4XiXMx-KBkbQ95zvjWLhqVjlkcjU7wu-ovPVSTAY', 1744708159, 'admin'),
('2248', 'f0b53b2da041fca49ef0b9839060b345', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjI0OCIsImV4cCI6MTc0NDc4NjA5NX0.kKPrHjL_8I0wodiSSXCBnwFAtherZDo74X1HG7bIBbk', 1744766295, 'member'),
('2259', '738116e65b4f68988b814bf341723e94', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMjU5LCJyb2xlIjoiQ291bmNpbCIsImV4cCI6MTc0NDg0MTI5OX0.xVgxCbkZeoeoJLvwYYu7eY6sTrIMeyxSuXPJPDnEJ-8', 1744841299, 'Council'),
('2260', '7f6fa37f06a1f57c833ac4d536ea3b95', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMjYwLCJyb2xlIjoiRW1wbG95ZWUiLCJleHAiOjE3NDQ4NDEyOTh9.wjOh3xziAxs2T12b0D8rxhu_5NYwdZCirIVOC7vkcf0', 1744841298, 'Employee'),
('2264', '638e9fef50d78200b3b338dbc94588d0', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMjY0LCJyb2xlIjoiU3R1ZGVudCIsImV4cCI6MTc0NDg0MTI5OX0.nMv4bRmshZ-WR71CPVT2TJAm2VEVLNAKve7O1A51gSU', 1744841299, 'Student'),
('2266', 'cd7a6820767129636a2eb37058803aa57e87359907b930cc9a70e2d3bc9e45ec', '21kUBPeneWUl91R0n4OSo3rCEOKWAFJp', 4346653, 'Visitor'),
('2270', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('23', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('24', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('24210094', '$2b$05$.r3fbqxrPM4/NznJLeeWfev.fUnpqNyadFbPOmdjVClGJZmA9h5gm', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAwOTQsInVzZXJuYW1lIjoiS0RvdCIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzQ0NzM0ODUyLCJleHAiOjE3NDQ4MjEyNTJ9.g5IuTVBVvgTdyFB7YOMMfnB5G1gfaLygIlS2zbRDkCE', 1744821252, 'user'),
('24210098', '$2b$05$87pwwGpP9wKW986RQ9hqkOjJBBb61aLKYZ7NmoptufS4SxbRi9Z3i', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAwOTgsInVzZXJuYW1lIjoicGEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ3MzQ5NzEsImV4cCI6MTc0NDgyMTM3MX0.S09-CzmX409XVFcF2yKgDYyOh6adEngUuRen0zV12jI', 1744821371, 'admin'),
('24210099', '$2b$05$plwcyDTWnhNE6lcDUeFkR.LvqflyKhojOiBcsSVZcXw.Rt5UIb7pS', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAwOTksInVzZXJuYW1lIjoiTVNQIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzQ0NzM0OTc0LCJleHAiOjE3NDQ4MjEzNzR9.3uD4tQkULgCy_sJwjcKxX1o7_Eyem_IN7OfqMYicdwQ', 1744821374, 'admin'),
('24210101', '$2b$05$BGXs/MznU9hEgx.ehoQ5yeWhT4VwgU/v4pZ0/BnegtPiogG5kxx4K', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAxMDEsInVzZXJuYW1lIjoiUmFuZG9tMSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzQ0NzM1MTk2LCJleHAiOjE3NDQ4MjE1OTZ9.zuhtMEAk6xGtR-_8DDhDQT-8aStIdwZ9BlYEKRmFWOM', 1744821596, 'user'),
('24210109', '006d2143154327a64d86a264aea225f3', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiUEciLCJyb2xlIjoidGVjaG5pY2lhbiIsImV4cCI6MTc0NDc3NTc1NiwiZ3JvdXAiOm51bGwsInNlc3Npb25faWQiOjI0MjEwMTA5fQ.khC2KDSsY6CoHNm4Pwf6Y1zNVFwClyBvha6HvJ83fB4', 1744755957, 'technician'),
('24210111', '72c48c6705bb0deb6969d802f215f534', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjQyMTAxMTEiLCJleHAiOjE3NDQ3MzYyMTh9.3Gd0xkW65a2wdKlTxqSnVnBM_oMMN4VRoXcThLNiUaY', 1744716419, 'member'),
('24210112', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('24210115', '628b5b4baf07120cc669fb6ce2a1ca72', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjI0MjEwMTE1IiwiUm9sZSI6ImFkbWluIiwiZXhwIjoxNzQ0NzkwMzgzfQ.tQc4vGy9DdVClMpnTrgeB5_ZmivhmdDuaB_31OpQw3M', 1744790383, 'admin'),
('24210117', 'e9335e177b288c7af4af8f1225c3f938', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyNDIxMDExNyIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDczOTIzMSwiZXhwIjoxNzQ0NzQyODMxfQ.alayUunF1kUstKe5fSm2rvbl338hX_IeCZ8m_oOxIpY', 1744742831, 'admin'),
('24210118', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'player'),
('24210119', '53526bf5efa884e4c5e115f2a00a8e74', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjQyMTAxMTkiLCJleHAiOjE3NDQ3ODYyOTN9.q0MqK-GEHKhEJ-EypxvPLt3TCV6iuSmVGffgh86NSWY', 1744766494, 'admin'),
('24210120', '$2b$05$rjwXuhu8JCa9i0j1Di8Ecug8wTWVS5wcoGl5UXGdHHk5rFHpTf4Mq', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjI0MjEwMTIwIiwidXNlcm5hbWUiOiJIaWlpX2FkbWluMiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDc2NTM4NCwiZXhwIjoxNzQ0ODUxNzg0fQ.3nQHLnXRULQ6lhXgR_gCbv4ReNycXrIy9xmDBhe28RE', 1744851784, 'admin'),
('24210127', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('24210128', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210130', 'securePassword123', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYnJhdmUiLCJyb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDc4MzE0NSwiZ3JvdXAiOjEyLCJzZXNzaW9uX2lkIjoiMjQyMTAxMzAifQ.6VSba5HuQGepuyE4IlXH4qQs3QlW8MyNn6MzJ-YKDas', 1744783145, 'student'),
('24210132', '0350b623313bc948e33f74cb67f5765b', NULL, NULL, 'Student'),
('24210133', '268f868a230bc3be2747329cc435ae72', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjQyMTAxMzMiLCJleHAiOjE3NDQ3NDc4ODZ9.u0U9gt4jWEqYuoo1yUBh9jgqpSm6G_1LPungmXZcGe0', 1744728086, 'member'),
('24210137', 'a356c7962bac989c4743b5ae03cf9ddb', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSFNTIiwicm9sZSI6Ik1hbmFnZXIiLCJleHAiOjE3NDQ3ODMxOTEsImdyb3VwIjoiMTEiLCJzZXNzaW9uX2lkIjoyNDIxMDEzNywiaWF0IjoxNzQ0Nzc5NTkxLCJqdGkiOiIxYjNmNWMyNzViZWM5NGU4NDNjMWExMTJiMjI1YmU2OCJ9.btSkl0oG6OoRLHczO0GCM47wgLw3KM2wvIw6PQBbwBg', 1744783191, 'Manager'),
('24210140', '44c72e9f21a0ef3b217ddffa09329e90', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjQyMTAxNDAiLCJleHAiOjE3NDQ3NTQxNDZ9.ndaMmaEfhaosPY3x5amWr3ou6LzLAJciC3ld1QIPnec', 1744734346, 'member'),
('24210143', '5f4dcc3b5aa765d61d8327deb882cf99', NULL, NULL, 'Manager'),
('24210144', '5f4dcc3b5aa765d61d8327deb882cf99', NULL, NULL, 'Manager'),
('24210145', '5f4dcc3b5aa765d61d8327deb882cf99', NULL, NULL, 'Manager'),
('24210146', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('24210151', '$2b$05$pozOdClIaAVKW0KZ8JRBl.VFM5tFO/nAzGT1mBgTxTQc5JfOYOefi', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjI0MjEwMTUxIiwidXNlcm5hbWUiOiJIaWlpX2FkbWluMyIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDc2MDg4OSwiZXhwIjoxNzQ0ODQ3Mjg5fQ.gcc4L-_LgCeVC0t29iIbcQ08-BZ5Y_u-iydm2XrO59s', 1744847289, 'admin'),
('24210153', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210154', 'afac0300566316123499bf11014b9a30aa2fa6a84a481b64ec1bfbffa2b6412c', '739620cf-c903-4f81-b92a-e6af4aeca3fc', 1744833482, 'admin'),
('24210156', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210157', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210158', 'af74a83ae0d5777401f86af4df941e98', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NDc0NjEyMiwianRpIjoiODI2MWM3NzktYWM3Mi00ZWYyLWE5ZDMtZTI4NjM5ZDgzMmE3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MjQyMTAxNTgsIm5iZiI6MTc0NDc0NjEyMiwiY3NyZiI6IjI4MzdmMGQ0LWFiNTEtNDY1OC04NWE4LWU1OTljZWU0ODhmOCIsImV4cCI6MTc0NDgzMjUyMiwicm9sZSI6IkVtcGxveWVlIn0.e1wyNOryL434y25uiCUez5Qu0FZYlQbWNx2vXgV7NY8', 1744832522, 'Employee'),
('24210164', 'c444858e0aaeb727da73d2eae62321ad', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjQyMTAxNjQiLCJleHAiOjE3NDQ3NTI1MjR9._UFMAVPNF-pgkXCDqXOHoGXpP_evxyYTWwU3iskTNYY', 1744732725, 'member'),
('24210166', '$2b$05$vdO/x6jZ8zltBRbKa.6oZeTyh50/2eh/kJDTuuJH0w3vZFwjW0nme', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAxNjYsInVzZXJuYW1lIjoiYXNkYXNkIiwicm9sZSI6InVzZXIiLCJpYXQiOjE3NDQ3NDY5MzgsImV4cCI6MTc0NDgzMzMzOH0.879ydoeRGyfAYYg7CSOPgekItwJnS33oP59SP8LJKlk', 1744833338, 'user'),
('24210167', '$2b$05$Vf9k698fPOO6h6ptKAnnMeHlueTS45tb4cC4Q8DGeh0ArZkx1Nly6', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjI0MjEwMTY3IiwidXNlcm5hbWUiOiJuaXNoaXQzNDU2Iiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzQ0NzQ5MjI0LCJleHAiOjE3NDQ4MzU2MjR9.BBi81CWQdn-Sc4joNTvI6D34TQE6VwmqLkyy6whRkVY', 1744835624, 'admin'),
('24210169', '$2b$05$15S1VyLkjCvoof.R.ooIsOjDjVOLQEJoJoFKho3QBSyl36QYUFZve', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjI0MjEwMTY5IiwidXNlcm5hbWUiOiJuaXNoaXQ5ODciLCJyb2xlIjoidXNlciIsImlhdCI6MTc0NDc0OTI1MSwiZXhwIjoxNzQ0ODM1NjUxfQ.V2Ki-aqZxnRjIwOKUkKkxKEpw5MkGyMls9Xw2eqAXBY', 1744835651, 'user'),
('24210170', '853006f06462856b42c2e3b4ffebb1a9400b9be81b4217ca71115f21cf81958b', 'da64ced4-afba-4c81-992c-03481d4c3c8b', 1744851518, 'Manager'),
('24210176', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210177', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210178', 'defaultPassword', NULL, NULL, 'user'),
('24210179', 'f6c2fda430a85b6c04930ffcb97b14e6', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjQyMTAxNzkiLCJleHAiOjE3NDQ3ODExNjh9.59obb-BpjFfsLxyJdADtT9P5p_mx8JGGlEFTFpdKXhg', 1744761368, 'member'),
('24210192', 'scrypt:32768:8:1$rrMDfSFgUqGBOOrd$ab338a6603bbe723c9aedb9c2ee576b9c50618278d2376be48051bb3431601681219f8665064f9e966ea6e9dfc21db7c3f854fb003a2033add2b05837171a6b5', NULL, NULL, 'user'),
('24210194', 'scrypt:32768:8:1$mCfe1OL39zxGcSb5$d16fe39c46c9d9073d626c098a108bff4487af1640d227555d133460c833b20ecda172de87c3bd347ebc8a179205b5912daad29777b357b33f2faf172bc0eca5', NULL, NULL, 'user'),
('24210196', 'scrypt:32768:8:1$2uqJYUOKSbvplrZy$7b9ac9d1ec6994d33b53f5b8a45db4a5fbfb047f6ba391a5140b4a433c0c25139c4ec941f5f80de8e6861950ef1ed4056559a9fc64384fb6b87857b1b4ff7478', NULL, NULL, 'user'),
('24210197', 'scrypt:32768:8:1$4xO98u9W5EAA9kuV$28d5047f0257b53fb21718f494248c3b45eab44ec1be06fb808eff8b85c741150cf87ab72296cfceb01f553274c6bcb793b90aa82f00b8c26938b7cd154151ee', NULL, NULL, 'user'),
('24210198', '628b5b4baf07120cc669fb6ce2a1ca72', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjI0MjEwMTk4IiwiUm9sZSI6InN0dWRlbnQiLCJleHAiOjE3NDQ3NTUwNzZ9.hjXcEek72M7La50WTd2BPgf81EPY0W9pBX1HE3br7Ac', 1744755076, 'student'),
('24210199', 'scrypt:32768:8:1$2jAIIi3UDamEOhP6$3f07098898f0caf3326fde6dc828d6395ac68a5c214e1b4427509c5043d8a16382a41b22a0844194073c1d667916a9984417401ec38dc8719fd1b629ccc79640', NULL, NULL, 'user'),
('24210201', 'scrypt:32768:8:1$ev8QbtAmYMTHS96M$5d5e06c7a7ed0b12af767dc756caed764cf8ebc8713927764bdec2e148a6235b37d95359c421e13d3436e285921b0d164076db9dfcff44c47dd6c6c9bcb99cc3', NULL, NULL, 'user'),
('24210202', 'scrypt:32768:8:1$SCZeVnbekKhtJQxS$f310287c65ef961f68bc22d0aa5d149c3654227f33fe0695d54e30b9455dfa8e41735bbe7326c9a844cdacd3f7501e0fdf85d9507b9e9229b343daaa3120f66d', NULL, NULL, 'user'),
('24210204', 'scrypt:32768:8:1$nuAT5cZib9MiY61M$7336255e0c7d1b3413279541a01cbf5761c6396ee83abcdbe37caa00ce0cd88a67a43e606345322d7edb3c1c57f1cf8f0f53ee1d82eff9a749662a232becae46', NULL, NULL, 'user'),
('24210213', 'f673d9991a246dbce15d315e7716bc1f', NULL, NULL, 'student'),
('24210215', '628b5b4baf07120cc669fb6ce2a1ca72', NULL, NULL, 'student'),
('24210216', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyNDIxMDIxNiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzQ0NzU2MTEyLCJleHAiOjE3NDQ3NTk3MTJ9.yia5pLxvogUXABFUJF3tFWiuoWcKI_gjsXXuLXpZFbk', 1744759712, 'user'),
('24210218', 'f673d9991a246dbce15d315e7716bc1f', NULL, NULL, 'student'),
('24210219', '79835ea3522d3f99a86de822097693ca', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjQyMTAyMTkiLCJleHAiOjE3NDQ3NTQxNjJ9.3HiHJbdRqHJBfymsWbmoHCNc6_vbTKLPGlRn5Kza6aE', 1744734363, 'member'),
('24210220', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210221', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210223', 'ce67bc446cf7525952e04c10d5a54a9c', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjI0MjEwMjIzIiwiUm9sZSI6InN0dWRlbnQiLCJleHAiOjE3NDQ3NjI3NjJ9.crdzri6Y4XozC7yB4c4r1hGtmtZ1EqTX4mlja5Pj9i0', 1744762762, 'student'),
('24210224', 'scrypt:32768:8:1$vrfSHauVkHcOcCqk$af3df8a97d44e83fa0deb29f971c0f19404bd7d2ef775046b5d5fa8c555f5a1cbcea312a51d021c36a0ecbd69bc9f4820d338fc4011754042a496c2f20242091', NULL, NULL, 'Visitor'),
('24210225', 'scrypt:32768:8:1$fw6oLLTlTyVYW8HP$b7d90174a9a2ed18dda5c445b9bbd027933d41c6b64663ccebfae715817b03fce82d85908adaf9d5c12c57d72d6002f3ee39f78798ec6ed7d3cc96dc3e8f1fc8', NULL, NULL, 'Student'),
('24210226', 'scrypt:32768:8:1$noHpOQEEAifWZBM1$bed99eb3e4b474a5364d23150012c5af59e976f9a8f15c809e18c981ab9069f24836cd4daf36d06ed40b62cea1ebeda88251e9a012437f07e0a13b13a76ea269', NULL, NULL, 'Student'),
('24210227', 'scrypt:32768:8:1$ZKYSVKQXrwtVTK9E$315cf02ab9d2a40fca49e1645533fed63b09eef08fb4840cef5878e8e9558d0d16c494b050550bd1ef19a25ba1c61492a2cdebe99b927c5d109c5e4dbb0ac01f', NULL, NULL, 'Visitor'),
('24210228', 'scrypt:32768:8:1$hoUxbPxk3H8qB20y$e6bf79ad02cc53190c6eeab81e5b39adc8405461bc97f282656a66bc591d0d53dbd7a68baec7ae296d70ad4f8b30560ba8ec9e7f216bfdbe4ed0f611c6d76a44', NULL, NULL, 'Student'),
('24210229', 'scrypt:32768:8:1$AsqIEE3PDafDUUF0$b05499a9f8eef48468fce24cb3aeb9ab87735d0b15e29093ee339d8091358f4a9c4346ef70cd1343e7142d4c65b0936169ec87d5a2b78c81ba9b09bd6d703178', NULL, NULL, 'Staff'),
('24210230', 'scrypt:32768:8:1$VHOx1QNeyMG2zKmR$1dc10b3b286c4d1822dd57056f4260826c255918673fdb4ba6dc4f545c012cd5ad07038ca9e2529c491604ad51b965706081502dbaf912cb78968d9e7b0c8084', NULL, NULL, 'Visitor'),
('24210231', 'scrypt:32768:8:1$Q34bqB6tfD3lRZSn$4c52a3b668e9f0d8d9fb1994e88c7fbacb082316ea70d6b10fa8dffe27662ac8d80aa588ce4e2548f587a32b176907de04fb307f870c380793b5150f9135edc3', NULL, NULL, 'Staff'),
('24210232', 'scrypt:32768:8:1$PBSChipPwB8hnYzJ$5eac5938231c870dc60b3e4dec1d69c68a0c9be0e12af79c9bea73aa81a9adbd0cb03723230b7c43cddaed5683e5920977147c2ccec95121c34193750233f0e4', NULL, NULL, 'Visitor'),
('24210233', 'scrypt:32768:8:1$vmrvAr1nz71GfXMf$82adb8749c06358dfd25edd37aef5bba55887478435d01ce0d89346a4eb9d29c97aaed8a70ad1d13edd8131bf4219648d4f4a011fc0ddaf59a303e7d1a73154e', NULL, NULL, 'Visitor'),
('24210234', 'scrypt:32768:8:1$auTgA5a2hqGk2mv0$d989dd39ae66ebf24ad3fcdc505a6f05565a3952ae8df6dfe7f64ee38afcc6d4058d6cc705cf06f87eeda7b947517917542e1b52d82adb627ef082e9b4e1af21', NULL, NULL, 'Staff'),
('24210235', 'scrypt:32768:8:1$78sTtaTZE4Ipybdo$4de6644dcb13144b32dbd860f7156719002e0e29835f320558bf571af68532fe2a1e993ae3ef20e09f5d799c519c7d939cf644feb61f64d2cebd628725352085', NULL, NULL, 'Staff'),
('24210236', 'scrypt:32768:8:1$0hFQq1WQYvr2QpaL$42cf57f27bf43908afca28910c5e63d233e03b20ccd9f655f46c88dd7e790e0521516d5930989b425f6993e75635f4106f10ea78fb64ad83d474183d9b8e3966', NULL, NULL, 'Staff'),
('24210237', 'scrypt:32768:8:1$JSSBKujAQHXABs8A$fd5931bbf8dd3e1fae04fc9f6ccceb8236cfe0780d552f08dad72a3c448ebc615420708022f93d1424b9360fd9a7dd45cbfa560f7827d526b71f322b9628bc71', NULL, NULL, 'Visitor'),
('24210238', '86f500cd7b7d38e5d4ae6cde3920f589', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicGl5dXNoIiwicm9sZSI6Ik1hbmFnZXIiLCJleHAiOjE3NDQ3OTA5MTgsImdyb3VwIjoiMTEiLCJzZXNzaW9uX2lkIjoyNDIxMDIzOCwiaWF0IjoxNzQ0Nzg3MzE4LCJqdGkiOiJjYWVmMWVkODM3NjYxMjIyZDM1ZTU5NmEwMTE2MmRkNiJ9._bG6uCif2xvwXf7TlGDWxMZztosOZ41U4_EFyQ1pf-E', 1744790918, 'Manager'),
('24210240', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('24210241', '2865a5b14e5a70273a7d311bfc150f4f', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoic2luZ2giLCJyb2xlIjoiTWFuYWdlciIsImV4cCI6MTc0NDc4NjMzMywiZ3JvdXAiOiIxMSIsInNlc3Npb25faWQiOjI0MjEwMjQxLCJpYXQiOjE3NDQ3ODI3MzMsImp0aSI6IjNjNmE1MGE3MzY4ODQ0YTI3ZDgwNGY2Y2U3NTc3OTVjIn0.d-mHlfekWlUJZ722D5S45TZ9Hf6n5c2GLVqaRXWH13U', 1744786333, 'Manager'),
('24210242', '64a43b6ca15d128ac6a0679b39bc9c07', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjQyMTAyNDIiLCJleHAiOjE3NDQ3NTk1NTh9.Kt7sx7hqaobVUkH3lM_Am2jwMIHOe_RyZydOpOrV2S4', 1744739758, 'member'),
('24210243', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyNDIxMDI0MyIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzQ0NzYzNzAwLCJleHAiOjE3NDQ3NjczMDB9.2Gp-oPQJt4RIfko6cfznQviwPDBlXBc3FIn-Mnk47Cg', 1744767300, 'user'),
('24210245', 'a9c8b29fc1faff4c0cfee99c15b1961fedcd4d3a42ebf825395d1c920f94cd32', 'ccbfa9ca-4be4-43db-a20e-420f4544b9c5', 1744869015, 'Admin'),
('24210246', '2c62e6068c765179e1aed9bc2bfd4689', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NDc2ODYwMCwianRpIjoiMjFiZDgwYjgtNDU1MS00ZmI5LWE1NTQtNjgzYjJjOTkwMTNmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MjQyMTAyNDYsIm5iZiI6MTc0NDc2ODYwMCwiY3NyZiI6IjA4OTU4ZDdmLTZhZWQtNDE2OS1iNjc2LWI2MmUzZjE3NjM3OSIsImV4cCI6MTc0NDg1NTAwMCwicm9sZSI6IlN0dWRlbnQifQ.cshlKxpITmu560QB2P8AjtcEmeuCYBxu-zyWZNWDSVU', 1744855000, 'Student'),
('24210253', '482c811da5d5b4bc6d497ffa98491e38', NULL, NULL, 'member'),
('24210254', 'scrypt:32768:8:1$KvAcZT4Ns5uNMAHr$182ebc98a4ea8de58cfd7410ac3db92ab6337ee1ae96e2ad6640692255c0b3744fb19a3a6f1e43a8b8066dea867616c7739e51b7357b7e55ab8471720589b342', NULL, NULL, 'Student'),
('24210259', '4aa5e325b908c8f40ca2eea7e3ac7846', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjQyMTAyNTkiLCJleHAiOjE3NDQ3NjI4NjZ9.qvg_IWDAfg1SvdEnKzON0SpBE2R5h357HG3reyDIUcs', 1744743067, 'member'),
('24210260', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('24210262', 'b231ac807865cc671f2f05e5bf42068f', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjQyMTAyNjIiLCJleHAiOjE3NDQ3NjMyODZ9.lAVwU4TB2Ufb_tTP_6ovQjhirKpk6kVAp9zzLvuIRTs', 1744743487, 'member');
INSERT INTO `Login` (`MemberID`, `Password`, `Session`, `Expiry`, `Role`) VALUES
('24210263', 'f87dab8d027236545a2257c668603a4d', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjQyMTAyNjMiLCJleHAiOjE3NDQ3NjQ0MTl9.lQuL9B7MWifJrD1lvhWG3fddUqgrtNjk3t4LylZbNZ0', 1744744619, 'member'),
('24210264', '$2b$05$ujGiqbAIG2vtKs3BdtgN0up6Ny49FcpzyyXluPbLFF80Jp7JHVl1m', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjI0MjEwMjY0IiwidXNlcm5hbWUiOiJTbWl0YSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzQ0NzgxODM3LCJleHAiOjE3NDQ4NjgyMzd9.m87LE895flkD--W7ZMumTjGqTE8Nog56YwWs8BA5NEM', 1744868237, 'user'),
('24210268', 'securePassword123', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibmFuZGluaSIsInJvbGUiOiJkb2N0b3IiLCJleHAiOjE3NDQ3ODEzMzgsInVzZXJfaWQiOiIyNDIxMDI2OCJ9.0m4AU87uPUKqM8viTYyVspCiNGcmgTA-yYWTwBGKwDE', 1744761538, 'doctor'),
('24210270', 'securePassword123', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicml0dSIsInJvbGUiOiJzdGFmZiIsImV4cCI6MTc0NDc4MzA2MCwiZ3JvdXAiOjEyLCJzZXNzaW9uX2lkIjoiMjQyMTAyNzAifQ.cSDx4vqyfoSI6-tyy3rCI_dKfq1n93UuIythWI6kWYk', 1744783060, 'staff'),
('24210271', 'AdminG1', NULL, NULL, 'admin'),
('24210273', 'd428c8b73ed63bc760b85b6e4bd044b5', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjQyMTAyNzMiLCJleHAiOjE3NDQ3Njc1OTF9.WdXio2XUKUlK_r8FNqVv09dJO5MhXov1y4cFFu58O-Y', 1744747791, 'member'),
('24210274', '$2b$05$qRGlUUsRmfAqtYFe86gfo.9nvEc.aLxI6aNvu4.pqiRlqNr6DhjL6', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjI0MjEwMjc0IiwidXNlcm5hbWUiOiJKYXllc2giLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ3ODIwMDEsImV4cCI6MTc0NDg2ODQwMX0.ZBaN4y8vXrVnM1tQoEOxZr8pFkY9ZHmubiMYYwPjP3I', 1744868401, 'admin'),
('24210276', 'scrypt:32768:8:1$o6XHR2OczsWD6JWQ$8dccbb5c4d307b5f52c446729ed4c02ce041cfb5b301ac5aae5c2cad0ba12d1b3c7ce1523a65818173199b0a4f02ea32d5ba65503e3b68971bbfb39b4d2f2e85', NULL, NULL, 'user'),
('24210277', '006d2143154327a64d86a264aea225f3', NULL, NULL, 'student'),
('24210278', 'scrypt:32768:8:1$o4DmAO1i25bQr39G$4c0de3f3dec29c7a6285a40c5571e7c9cb5483c6558c2f3014dbd48de95a49c4234bfd7586b22508487ecc68a6e438249b7e6d15fd865cf970aa70af61c21575', NULL, NULL, 'user'),
('24210279', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('24210280', '$2b$05$rlasABU2/l2ZYfmIDm/Iiue2Fo6.ryxpQ2D5NO0kvEfwhB06xL.9q', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAyODAsInVzZXJuYW1lIjoiQ2hpbiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzQ0NzczMjk3LCJleHAiOjE3NDQ4NTk2OTd9.uUeEfmzx6E3QGPqspgnrrDi3POGSF5bejDJLBgzRh5k', 1744859697, 'user'),
('24210282', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('24210284', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('24210286', '$2b$05$akR.ya/iKyHL.xcCOrFuF.SUv896e7vK/.bQY1YL1vB2aTRue8gxC', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAyODYsInVzZXJuYW1lIjoiYWRtaW4yMyIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDc3NTQxNCwiZXhwIjoxNzQ0Nzc5MDE0fQ.c750opVmI9EM8s0rknwElENVkVgfqdcFkmOWEBrExg8', 1744779014, 'admin'),
('24210287', '$2b$05$7XK1KgvJU0eNlVH41DQVj.z.SQVRCn40iYYJ1EXa5ZuJDgYiDoVbG', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAyODcsInVzZXJuYW1lIjoiTmlzaGl0IFByYWphcGF0aSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDc3NjQ5MiwiZXhwIjoxNzQ0NzgwMDkyfQ.9A_eb_hluSo3LhUuRlInw3YenzL_TWLfn9WPhPPhvDk', 1744780092, 'admin'),
('24210298', '$2b$05$YyDcpVyT3R.rAwQup5SPNen.7Y4/lmbZpacg4C5ufiAqXA76EHvly', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjI0MjEwMjk4IiwidXNlcm5hbWUiOiJOaXNoaXQgcHJhIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzQ0NzgwNTU5LCJleHAiOjE3NDQ4NjY5NTl9.CSfiGyp_rzWRHxewOrFl0v3TTuTS8O28spGhhJTZ3Rc', 1744866959, 'admin'),
('24210299', '$2b$05$wM3CWdtzrvPWfFJI9YmwT.dlmX.3Ofu2Q8mMBlZ3DQTcD2j/fbx3W', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAyOTksInVzZXJuYW1lIjoibmlzaGl0IHVzZXIiLCJyb2xlIjoidXNlciIsImlhdCI6MTc0NDc3OTg2NiwiZXhwIjoxNzQ0NzgzNDY2fQ.Zz9ofxOx_2ydmNJ8IrOjaNSBRF44ZFiQUYg52yryfAw', 1744783466, 'user'),
('24210300', 'scrypt:32768:8:1$YFltEZ2w9hNLGodt$4123bbef96b658dd4087bef9e0c32a9e88c5c1f6655a6ec551465da9eae2f3c1e4ddadae4b19e991135b17e8c4b1b3ff71a7489238a345c677b656ed6d835843', NULL, NULL, 'user'),
('24210301', '1234', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicmFodWwuc2hhcm1hQGV4YW1wbGUuY29tIiwicm9sZSI6InN0dWRlbnQiLCJleHAiOjE3NDQ3ODU0MDYsImdyb3VwIjoxMiwic2Vzc2lvbl9pZCI6IjI0MjEwMzAxIn0.iCc6FXVTu-e53GtKUPxiBwHeVw_esYkks543WeAI_ho', 1744785406, 'student'),
('24210302', '$2b$05$0QoZB8KwTGqjuXhakuMo4uEELAo5tcpcKRNKzK0gDOlYZxA4qxbHm', NULL, NULL, 'user'),
('24210303', 'scrypt:32768:8:1$XQCNXw7rIcH78Hph$1bc0b2adc8783f9e439a48a444616c35e1a4728e86e78732615807e55b5e919db52540093abf64c9c649d76f1e3da9250cd3662d020254c5576f2e0a42fe5925', NULL, NULL, 'user'),
('24210304', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210305', '2308aaae5d348ce8ab06010b88988227', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjI0MjEwMzA1IiwiUm9sZSI6InN0dWRlbnQiLCJleHAiOjE3NDQ3ODgwMjl9.Cu0aixq7kJC50vFpNe23i3xAptx6hbRHx-RDTfBGm_w', 1744788029, 'student'),
('24210306', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('24210307', '2308aaae5d348ce8ab06010b88988227', NULL, NULL, 'visitor'),
('24210308', '$2b$05$WcC3bMuEPJ/tEYbgl4Jhy.AO7CE6mHsBgEyyeSLj0BTQw5TGYH7NW', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjQyMTAzMDgsInVzZXJuYW1lIjoidXNlcjIzNCIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzQ0Nzg0NjI5LCJleHAiOjE3NDQ3ODgyMjl9.h993kEP1GsCdsGM9eMpIDP8yFbGgEHw2L591L0pfxR0', 1744788229, 'user'),
('24210310', '2308aaae5d348ce8ab06010b88988227', NULL, NULL, 'student'),
('24210311', '2308aaae5d348ce8ab06010b88988227', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjI0MjEwMzExIiwiUm9sZSI6InN0dWRlbnQiLCJleHAiOjE3NDQ3OTAwNDl9.FZQERc1hTHz2dvhaGFot8n1MoeR_4gRL-_jBAz0uxl8', 1744790049, 'student'),
('24210312', '2308aaae5d348ce8ab06010b88988227', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjI0MjEwMzEyIiwiUm9sZSI6InZpc2l0b3IiLCJleHAiOjE3NDQ3OTAzMTF9.fK_eABb2nbLMQzKA-h40mfcU7NKl-3UQ4-K5FSD0hG0', 1744790311, 'visitor'),
('25', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('26', '81dc9bdb52d04dc20036dbd8313ed055', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZW1iZXJfaWQiOiIyNiIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0NDQ4OTYyNC4wNjYwNzZ9.2SeWL-V1JePULL9WG1Xy-2AedcLxVB9AcakoBqQpff0', 1744489624, 'admin'),
('301', 'admin123', 'a640106c-7a79-4e34-b28d-cdef738ebdc7', 1744712942, 'admin'),
('302', 'admin123', 'd0aadb76-1b61-498d-b2dc-0d224d5eac73', 1744316933, 'admin'),
('31', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('35', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('36', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('38', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('446', '10edeabdb95b0d238cefc8cac7c383af', '', NULL, 'student'),
('447', '1234', NULL, NULL, 'admin'),
('450', '161ebd7d45089b3446ee4e0d86dbcf92', NULL, NULL, 'member'),
('455', '006d2143154327a64d86a264aea225f3', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdHVzZXIxMjMiLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NDQ3NzU0ODYsImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjo0NTV9.ha8dHYcacaekY3m0q2ubAtTNLxXjlWkatCSlQtt5Su4', 1744755686, 'admin'),
('456', '5627e974f66a9f51e41799a221120d9ec61af71b7af2d57cf98b8d30d2765f3c', '1ZjivgbwuEaKh2vL17cr0t4eustzs4yR', 8828715, 'Visitor'),
('457', '$2b$05$18.EghoP73pm/xdlP8XpX.lr5M07HR9NyOvdVo3pW8fjDB3Yxtmre', NULL, NULL, 'user'),
('49', '$2b$05$lJ2mBaoyVByqhr6Bz2iqdeIqw1Jw2pRRsrVtIaMPcX8cl1iOhk2EK', NULL, NULL, 'user'),
('5', 'Amit@123', NULL, NULL, 'security'),
('8', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('9', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `MemberGroupMapping`
--

CREATE TABLE `MemberGroupMapping` (
  `MemberID` int NOT NULL,
  `GroupID` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `MemberGroupMapping`
--

INSERT INTO `MemberGroupMapping` (`MemberID`, `GroupID`) VALUES
(456, 5),
(457, 10),
(1114, 5),
(1111, 6),
(1191, 5),
(1224, 15),
(1251, 8),
(1252, 8),
(1257, 8),
(1258, 8),
(1261, 10),
(1262, 10),
(1304, 10),
(1309, 10),
(424, 2),
(1310, 8),
(1312, 10),
(1407, 10),
(1411, 10),
(1413, 10),
(1419, 8),
(1435, 8),
(2001, 2),
(2002, 2),
(2003, 2),
(2004, 2),
(2005, 2),
(2006, 2),
(2007, 2),
(2008, 2),
(2009, 2),
(2010, 2),
(2016, 8),
(2017, 13),
(2019, 5),
(2021, 5),
(1176, 14),
(112, 15),
(1414, 3),
(2035, 1),
(2038, 1),
(2029, 7),
(164, 15),
(2049, 8),
(2056, 8),
(2065, 5),
(2072, 5),
(2080, 17),
(2083, 1),
(2084, 8),
(2087, 13),
(2088, 5),
(2089, 5),
(2092, 1),
(2093, 5),
(2094, 1),
(2096, 10),
(2097, 5),
(2099, 10),
(2100, 5),
(2102, 10),
(2103, 10),
(2104, 1),
(2105, 10),
(2106, 5),
(2109, 1),
(2110, 17),
(2111, 17),
(2112, 1),
(2114, 5),
(2115, 1),
(2116, 10),
(2118, 5),
(2125, 5),
(2138, 5),
(2141, 10),
(2149, 15),
(2162, 5),
(2163, 11),
(2164, 5),
(2166, 15),
(2167, 1),
(2168, 5),
(2176, 14),
(2191, 1),
(2197, 9),
(2198, 9),
(2200, 11),
(2202, 1),
(2217, 5),
(2219, 1),
(2235, 10),
(2236, 10),
(2239, 14),
(2241, 10),
(2242, 14),
(2244, 14),
(2248, 1),
(2259, 14),
(2260, 14),
(2264, 14),
(2266, 5),
(2267, 5),
(2268, 5),
(24210094, 10),
(24210098, 10),
(24210099, 10),
(24210101, 10),
(24210111, 1),
(24210120, 10),
(24210128, 3),
(24210132, 14),
(24210133, 1),
(24210140, 1),
(24210151, 10),
(24210154, 17),
(24210158, 14),
(24210164, 1),
(24210166, 10),
(24210167, 10),
(24210169, 10),
(24210170, 17),
(24210178, 15),
(24210179, 1),
(24210192, 8),
(24210194, 8),
(24210196, 8),
(24210197, 8),
(24210199, 8),
(24210201, 8),
(24210202, 8),
(22110206, 17),
(24210209, 5),
(24210219, 1),
(24210224, 5),
(24210225, 5),
(24210226, 5),
(24210227, 5),
(24210228, 5),
(24210229, 5),
(24210230, 5),
(24210231, 5),
(24210232, 5),
(24210233, 5),
(24210234, 5),
(24210235, 5),
(24210236, 5),
(24210237, 5),
(24210242, 1),
(24210245, 17),
(24210246, 14),
(24210253, 1),
(24210254, 5),
(24210259, 1),
(24210262, 1),
(24210263, 1),
(24210264, 10),
(2077, 7),
(24210273, 1),
(24210274, 10),
(24210280, 10),
(24210286, 10),
(24210287, 10),
(24210288, 3),
(24210289, 3),
(24210291, 3),
(24210292, 3),
(24210293, 3),
(24210294, 3),
(24210295, 3),
(24210296, 3),
(24210298, 10),
(24210299, 10),
(24210302, 10),
(24210304, 3),
(24210308, 10);

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `UserName` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ID` int NOT NULL,
  `emailID` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DoB` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`UserName`, `ID`, `emailID`, `DoB`) VALUES
('john_doe3', 4, 'john.doe@example.com', '1990-05-15'),
('temp10', 6, 'john.doe@example.com', '1990-05-15'),
('temp11', 7, 'john.doe@example.com', '1990-05-15'),
('temp12', 8, 'john.doe@example.com', '1990-05-15'),
('temp13', 9, 'john.doe@example.com', '1990-05-15'),
('temp14', 10, 'john.doe@example.com', '1990-05-15'),
('temp15', 11, 'john.doe@example.com', '1990-05-15'),
('temp16', 12, 'john.doe@example.com', '1990-05-15'),
('temp18', 14, 'john.doe@example.com', '1990-05-15'),
('temp20', 16, 'john.doe@example.com', '1990-05-15'),
('temp22', 18, 'john.doe@example.com', '1990-05-15'),
('temp23', 19, 'john.doe@example.com', '1990-05-15'),
('temp25', 21, 'john.doe@example.com', '1990-05-15'),
('temp26', 22, 'john.doe@example.com', '1990-05-15'),
('temp27', 23, 'john.doe@example.com', '1990-05-15'),
('temp28', 24, 'john.doe@example.com', '1990-05-15'),
('temp29', 25, 'john.doe@example.com', '1990-05-15'),
('temp30', 26, 'john.doe@example.com', '1990-05-15'),
('temp32', 28, 'john.doe@example.com', '1990-05-15'),
('temp33', 29, 'john.doe@example.com', '1990-05-15'),
('temp34', 30, 'john.doe@example.com', '1990-05-15'),
('temp36', 32, 'john.doe@example.com', '1990-05-15'),
('temp37', 33, 'john.doe@example.com', '1990-05-15'),
('temp38', 34, 'john.doe@example.com', '1990-05-15'),
('temp39', 35, 'john.doe@example.com', '1990-05-15'),
('temp40', 36, 'john.doe@example.com', '1990-05-15'),
('pankaj', 38, 'john.doe@example.com', '1990-05-15'),
('samarth ', 49, 'nishitprajapati77@gmail.com', '2025-04-10'),
('NIYATI', 112, 'niyati@member.com', '2025-04-15'),
('Humpty', 127, 'humpty127@example.com', '2002-05-21'),
('Tanvi', 149, 'testuser@example.com', '2005-01-15'),
('DIYA', 150, 'DIYA@admin.com', '2005-11-07'),
('Neelam Tiwari', 160, 'neelam.tiwari@example.com', '2025-04-08'),
('Hamsika', 164, 'hamsika@gmail.com', '2025-04-15'),
('Maitri', 192, 'maitri@gmail.com', '2025-04-15'),
('Admin1', 301, 'admin123@example.com', '2002-01-15'),
('Admin2', 302, 'admin2@example.com', '2002-01-15'),
('Tusher', 424, 'tusher@gmail.com', '1990-05-15'),
('check', 444, 'check@check.com', '2022-11-11'),
('aarti2', 446, 'aarti2@example.com', '2000-01-15'),
('rama1', 447, '', NULL),
('johndoe', 450, 'johndoe@example.com', '1990-01-01'),
('testuser123', 455, 'testuser123@example.com', '2000-01-01'),
('ST20004', 456, 'balmukund@example.com', NULL),
('himanshu', 457, 'nishitprajapati7@gmail.com', '2004-11-11'),
('Rita', 1111, 'rita@gmail.com', '2025-04-02'),
('mitansh', 1112, 'nishitprajapati6@gmail.com', '1990-04-15'),
('V30002', 1114, 'manbhavan@gmail.vom', NULL),
('dd', 1118, 'dd@iitgn.ac.in', '2001-09-15'),
('new_test_user', 1122, 'test@example.com', '2000-01-01'),
('Vinay', 1124, 'vinay@gmail.com', '2004-07-30'),
('Sujith', 1125, 'sujith@gmail.com', '2003-10-07'),
('Sri Jahnavi', 1126, 'srijahnavi@gmail.com', '2005-01-01'),
('Siri Gangannagudem', 1127, 'siri@gmail.com', '2005-02-01'),
('Jethru', 1128, 'jethru@gmail.com', '2004-06-01'),
('test_user', 1129, 'test@example.com', '1990-05-15'),
('trialHelloCheck', 1130, '12345@example.com', '1990-05-15'),
('ansh', 1131, 'ansh@gmail.com', '2025-04-10'),
('ashutosh', 1132, 'ashu@gmail.com', '2025-01-01'),
('jiyan', 1134, 'jiyan@gmail.com', '2020-02-01'),
('Rohit', 1135, 'rohit@gmail.cpm', '2007-02-28'),
('vanshu', 1137, 'vanshu2006@gmail.com', '2006-01-24'),
('Manan', 1138, 'manan18@gmail.com', '2000-01-01'),
('krishansharma08052000', 1139, 'krishansharma08052000@gmail.com', '2001-07-14'),
('krishansharma08052', 1142, 'krishansharma08052@gmail.com', '2001-07-14'),
('mahi', 1143, 'msd7@gmail.com', '1983-07-07'),
('krishansharma', 1145, 'krishansharma@gmail.com', '2001-07-14'),
('krishansharma1', 1148, 'krishansharma1@gmail.com', '2001-07-14'),
('krishansharma2', 1150, 'krishansharma2@gmail.com', '2001-07-14'),
('Naveen Pal', 1151, 'naveenpal@iitgn.ac.in', '2006-12-26'),
('Prajas', 1152, 'zma@pok.com', '2025-04-14'),
('Charmender', 1154, 'pokemon@pokemon.com', '2025-04-14'),
('deepakkalal', 1159, 'deepakkalal@nonsence.com', NULL),
('Parrrth', 1162, 'kishan@iitgn.ac.in', '1990-05-15'),
('Parrrth Govale', 1163, 'kishan@iitgn.ac.in', '1990-05-15'),
('patel108', 1164, 'MIfTANsrt@gmail.com', '2004-10-10'),
('deepakkalal1', 1165, 'deepakkalal1@nonsence.com', NULL),
('Jiya Desai', 1166, 'jiyadesai@it', '1111-11-11'),
('balu', 1168, 'balu@gmail.com', NULL),
('balu1', 1170, 'balu1@gmail.com', NULL),
('testuser', 1175, 'testuser@example.com', '1990-01-01'),
('admin', 1176, 'admin@dinewell.com', '2000-01-01'),
('test_student', 1177, 'student@example.com', '2000-01-01'),
('new_user', 1178, 'new_user@example.com', '1995-06-15'),
('Harshith', 1182, 'venigalla.harshith@iitgn.ac.in', '2005-10-24'),
('Rachit Jain', 1185, 'rachit.jain@iitgn.ac.in', '2005-06-15'),
('kved', 1190, 'kishan.ved@example.com', '2004-08-15'),
('S10010', 1191, 'wasimkonain@gmail.com', NULL),
('jiyakishan', 1199, 'john.doe@example.com', '1990-01-01'),
('jiya_kishan', 1200, 'john.doe@example.com', '1990-01-01'),
('jiya_kishanved', 1201, 'john.doe@example.com', '1990-01-01'),
('jkv', 1205, 'aaa', '1990-01-01'),
('jkved', 1206, 'aaa', '1990-01-01'),
('jiyakved', 1207, 'aaa', '1990-01-01'),
('adminkiller', 1214, 'akak', '1990-01-11'),
('adminved', 1222, 'asdddf', '1990-01-01'),
('John Doe2', 1224, 'john2@example.com', '1990-01-02'),
('ZZZ Test', 1228, 'zzz@test.com', NULL),
('ZZ Test', 1230, 'zz@test.com', NULL),
('Test', 1232, 'testing@test.com', NULL),
('dew', 1239, 'dewans461@gmail.com', NULL),
('aa', 1244, 'dewans461@gmail.com', NULL),
('aa1', 1248, 'dewans461@gmail.com', NULL),
('abc', 1249, 'dewans461@gmail.com', NULL),
('Rajput', 1251, '23110269@iitgn.ac.in', '2025-04-14'),
('Kp', 1252, '23110021@iitgn.kp.in', '2025-04-14'),
('Meena', 1253, 'meena.curie@example.com', NULL),
('Ishikaa', 1256, 'ishika@example.com', '2003-08-15'),
('PrajasKulkarni', 1257, 'prajas@iitgn', '2025-04-01'),
('PrajasKulkarni123', 1258, 'prajaskulkarni@iitgn', '2025-04-12'),
('nishit_ch', 1259, 'nishitprajapati111@gmail.com', '2004-09-19'),
('nishit_ck', 1261, 'nishitprajapati111@gmail.com', '2004-09-19'),
('nishit_ckp', 1262, 'nishitprajapati111@gmail.com', '2004-09-19'),
('IshikaaPatel', 1300, 'ishika@example.com', '2003-08-15'),
('task1', 1301, 'task1@test.com', NULL),
('dewdew', 1302, 'abc@gmail.com', NULL),
('balu11', 1303, 'balu11@gmail.com', NULL),
('nishit_cknp', 1304, 'nishitprajapati111@gmail.com', '2004-09-19'),
('sushi', 1305, 'sushi@gmail.com', '2000-02-01'),
('sushi1', 1307, 'sushi1@gmail.com', '2000-02-01'),
('nishit_cknpmh', 1309, 'nishitprajapati2111@gmail.com', '2004-09-19'),
('Lakshya Kesarwani', 1310, 'lakshya@iitgn.ac.in', '2006-05-14'),
('JLate', 1311, 'j.late@gmail.com', NULL),
('senextjs', 1312, 'ue123@exam.com', '2000-05-15'),
('Jyoti Agarwal', 1400, 'jyoti@example.com', '2001-08-15'),
('Admin123', 1402, 'admin@safedocs.com', NULL),
('jane_doe', 1407, 'jane.doe@example.com', '1995-08-20'),
('24210057', 1408, '24210057@iitgn.ac.in', '2001-07-14'),
('jane_de', 1411, 'jane.doe@example.com', '1995-08-20'),
('jane_xdfcfve', 1413, 'jane.doe@example.com', '1995-08-20'),
('test_admin', 1414, 'admin@gmail.com', '2003-09-01'),
('242100572', 1417, '242100572@iitgn.ac.in', '2001-07-14'),
('242100573', 1418, '242100573@iitgn.ac.in', '2001-07-14'),
('adil', 1419, 'adil@gmail.com', '2025-04-02'),
('Paresh', 1428, 'paresh@gmail.com', '2025-04-10'),
('jane_nishit', 1430, 'jane.doe@example.com', '1995-08-20'),
('rahul', 1435, 'rahul@gmail.com', '2025-04-14'),
('john_doe', 2001, 'john.doe@example.com', '1995-05-14'),
('jane_smith', 2002, 'jane.smith@example.com', '1993-08-23'),
('mark_jones', 2003, 'mark.jones@example.com', '1990-12-17'),
('alice_white', 2004, 'alice.white@example.com', '1997-03-05'),
('bob_brown', 2005, 'bob.brown@example.com', '1996-02-10'),
('carol_green', 2006, 'carol.green@example.com', '1994-06-25'),
('david_blue', 2007, 'david.blue@example.com', '1992-11-30'),
('emily_purple', 2008, 'emily.purple@example.com', '1998-09-19'),
('james_yellow', 2009, 'james.yellow@example.com', '1991-07-21'),
('susan_red', 2010, 'susan.red@example.com', '1995-04-18'),
('TS Kumbar', 2011, 'tskumbar@iitgn.ac.in', '2004-06-08'),
('Member 1', 2014, 'member@example.com', '2000-01-01'),
('Ramesh ', 2015, 'ramesh.singh@example.com', '1990-05-15'),
('jaggu', 2016, 'jaggu@gmail.com', '2025-04-09'),
('nevergonna', 2017, 'giveup@gmail.com', '2025-04-08'),
('Someone', 2018, 'someone@gmail.com', NULL),
('1w6qtfdt@example.com', 2019, '1w6qtfdt', NULL),
('kartikpillai@example.com', 2021, 'kartikpillai', NULL),
('sushi2', 2022, 'sushi2@gmail.com', '2000-02-01'),
('CRinku', 2023, 'c.rinku@example.com', NULL),
('sushi3', 2024, 'sushi3@gmail.com', '2000-12-24'),
('nishit_cknpmh2', 2025, 'nishitprajapati2111@gmail.com', '2004-09-19'),
('JehtruNew', 2026, 'j@email.com', NULL),
('Kamal Hasan', 2027, 'kamal.hasan@example.com', '1920-05-15'),
('CR', 2028, 'cr.curl@example.com', '2010-10-10'),
('admin143', 2029, 'admin@431', NULL),
('WhoRU', 2030, 'who.ru@example.com', '2010-10-10'),
('nimitt', 2031, 'nimitt.nimitt@iitgn.ac.in', '2004-09-20'),
('testtt2', 2035, 'aaaaa2', '1990-01-01'),
('Rachit Singh', 2037, 'rachitjain@gmail.com', '2005-05-22'),
('testtt22', 2038, 'aaaaa22', '1990-01-01'),
('1233', 2046, '1233@gmail.com', NULL),
('1234', 2048, '1234@gmail.com', NULL),
('kulkarni', 2049, 'kulkarni@iitgn', '2025-04-14'),
('1235', 2050, '1235@gmail.com', NULL),
('1239', 2052, '1239@gmail.com', NULL),
('bus', 2054, 'bus.bus@example.com', '2001-01-01'),
('vivek', 2056, '23110200@iitgn', '2025-04-30'),
('1211', 2057, '1211@gmail.com', NULL),
('Zagu Sussu', 2058, 'zagu@gmail.com', '2006-01-14'),
('12000', 2059, '12000@gmail.com', NULL),
('deepa', 2061, 'deepa@nonsence.com', NULL),
('Giniii', 2062, 'ginni@gmail.com', '2025-04-11'),
('deepa1', 2064, 'deepa1@nonsence.com', NULL),
('vibhajoshi@example.com', 2065, 'vibhajoshi', NULL),
('deepa2', 2066, 'deepa2@nonsence.com', NULL),
('deepa22', 2068, 'deepa22@nonsence.com', NULL),
('zags', 2069, 'zags@gmail.com', '2025-04-02'),
('deepa222', 2070, 'deepa222@nonsence.com', NULL),
('deeepa222', 2071, 'deeepa222@nonsence.com', NULL),
('chandanrana@example.com', 2072, 'chandanrana', NULL),
('raghu2', 2073, 'raghu2@a.com', NULL),
('raghu22', 2074, 'raghu22@a.com', NULL),
('avinash2', 2078, 'avinsh@143', NULL),
('Rahul Jain', 2080, 'jain.rahul@iitgn.ac.in', '1995-05-22'),
('nimitt2', 2081, 'nimittnim@gmail.com', '2004-09-21'),
('nimitt3', 2083, 'nimittijbaf', '2004-09-21'),
('Rohit Sharma', 2084, 'rohit@gmail.com', '1989-01-17'),
('24210032', 2086, '24210032@iitgn.ac.in', NULL),
('chillguy', 2087, 'neverchill@gmail.com', '1947-08-15'),
('mohitbhattacharya@example.com', 2088, 'mohitbhattacharya', NULL),
('sunilrawat@example.com', 2089, 'sunilrawat', NULL),
('nimitt4', 2092, 'nimitt.nimitt', '2004-09-24'),
('dhruvgill@example.com', 2093, 'dhruvgill', NULL),
('iu', 2094, 'iu', '1990-01-01'),
('Dipesh', 2095, 'dipesh@example.com', '1990-01-01'),
('shilpapatel@example.com', 2097, 'shilpapatel', NULL),
('rameshvaidya@example.com', 2100, 'rameshvaidya', NULL),
('jiyadesai', 2104, 'jiyadessaiemail', '2000-05-12'),
('Person12', 2105, 'dummy@gmail.com', '2005-01-01'),
('namitavarma@example.com', 2106, 'namitavarma', NULL),
('jiyadesai2', 2107, 'jiyadesaiemail', '2000-05-12'),
('jiyadesai22', 2109, 'jiyadesaiemail', '2000-05-12'),
('Go_Insta', 2110, 'go_insta@iitgn.ac.in', '1990-01-01'),
('Amit Kumar', 2111, 'kumar.amit@iitgn.ac.in', '1990-01-01'),
('tryagain', 2112, 'tryagainemail', '2000-02-12'),
('krishansh', 2113, 'krishansh@aa.com', NULL),
('rekhabhattacharya@example.com', 2114, 'rekhabhattacharya', NULL),
('ui', 2115, 'ui', '1990-01-01'),
('KendrikLamar', 2116, 'KDot@gmail.com', '1987-06-17'),
('bus1', 2117, 'bus1.curl@example.com', '2001-01-01'),
('shivanikapoor@example.com', 2118, 'shivanikapoor', NULL),
('deep', 2119, 'newuser@example.com', '1990-01-01'),
('deep-1', 2120, 'newuser@example.com', '1990-01-01'),
('deep-2', 2121, 'newuser@example.com', '1990-01-01'),
('aaaa', 2123, 'a@b.c', NULL),
('varshik', 2124, 'j@123', NULL),
('S10011', 2125, 'sumanbhardwaj@gmail.com', NULL),
('new_admin', 2126, 'a@b.c', NULL),
('vars', 2127, 'admin@123', NULL),
('a', 2128, 'a@b.c', NULL),
('avdbdfh', 2135, 'ab@b.c', NULL),
('ade', 2136, 'ab@b.c', NULL),
('Goud', 2137, 'goud@gmail.com', NULL),
('S10012', 2138, 'rutujaswami@gmail.com', NULL),
('goud2', 2139, 'alice@example.com', NULL),
('nishit_cknpmh23', 2141, 'nishitprajapati2111@gmail.com', '2004-09-19'),
('2005', 2142, 'new.curl@example.com', '2003-04-03'),
('iamnewhere', 2144, 'new.here@example.com', '2020-01-01'),
('krish', 2145, 'krish@gmail.com', NULL),
('krish111', 2148, 'krish111@hostel.edu', NULL),
('John Doe3', 2149, 'john3@example.com', '1990-01-03'),
('Vraj Shah', 2157, 'vraj.shah@iitgn.ac.in', '2004-11-28'),
('100', 2160, 'new.curl@example.com', '2003-04-03'),
('Umashree', 2161, 'new.curl@example.com', '2003-04-03'),
('saritaphadke@example.com', 2162, 'saritaphadke', NULL),
('MP', 2163, 'MP@gmail.com', '2004-03-01'),
('S10013', 2164, 'aniketasati@gmail.com', NULL),
('John Doe4', 2166, 'john4@example.com', '1990-01-04'),
('JiyaFinalTest', 2167, 'jiyafinaltestemail', '1990-02-12'),
('S10014', 2168, 'weired@example.com', NULL),
('User', 2172, 'user@gmail.com', NULL),
('Dewansh Singh Chandel', 2174, 'dewanshsingh.chandel@iitgn.ac.in', '1111-11-11'),
('TestUsr3', 2176, 'testusr3@example.com', '2003-04-05'),
('Tusharr', 2188, 'new.curl@example.com', '2003-04-03'),
('asd', 2189, 'asd', '1111-11-11'),
('asda', 2191, 'asda', '1111-11-11'),
('Bharathi', 2192, 'new.curl@example.com', '2003-04-03'),
('DP', 2193, 'new.curl@example.com', '2003-04-03'),
('AryanSahu', 2197, 'aryan.sahu@iitgn.ac.in', NULL),
('Dewansh Kumar', 2198, 'dewansh.kumar@iitgn.ac.in', NULL),
('abcd', 2199, 'efgh', '2000-02-02'),
('PB', 2200, 'PB@gmail.com', '2025-04-16'),
('abcde', 2202, 'efgh', '2000-02-02'),
('krish11111111', 2203, 'krish11111111@gmail.com', NULL),
('jhinknk', 2204, 'jhinknk@efdfdf.com', NULL),
('balu11111', 2208, 'balu11111@gmail.com', '2001-01-01'),
('OurAdmin', 2209, 'demo@task5.com', '1900-04-03'),
('OurCoach', 2210, 'demo@task5.com', '1900-04-03'),
('OurOrganiser', 2211, 'demo@task5.com', '1900-04-03'),
('OurOrganiser1', 2213, 'demo@task5.com', '1900-04-03'),
('OurReferee', 2214, 'demo@task5.com', '1900-04-03'),
('OurEqManager', 2215, 'demo@task5.com', '1900-04-03'),
('OurPlayer', 2216, 'demo@task5.com', '1900-04-03'),
('V30003', 2217, 'kritikamishra@gmail.com', NULL),
('OurOrganizer', 2218, 'demo@task5.com', '1900-04-03'),
('kishna', 2219, 'kishan@gmail.com', '2004-01-01'),
('OurCoach2', 2220, 'demo@task5.com', '1900-04-03'),
('OurPlayer1', 2221, 'demo@task5.com', '1900-04-03'),
('OurPlayer2', 2222, 'demo@task5.com', '1900-04-03'),
('OurPlayer3', 2223, 'demo@task5.com', '1900-04-03'),
('OurPlayer4', 2224, 'demo@task5.com', '1900-04-03'),
('OurPlayer5', 2225, 'demo@task5.com', '1900-04-03'),
('OurPlayer6', 2226, 'demo@task5.com', '1900-04-03'),
('OurPlayer7', 2227, 'demo@task5.com', '1900-04-03'),
('OurPlayer8', 2228, 'demo@task5.com', '1900-04-03'),
('OurPlayer9', 2229, 'demo@task5.com', '1900-04-03'),
('OurPlayer10', 2230, 'demo@task5.com', '1900-04-03'),
('OurPlayer11', 2231, 'demo@task5.com', '1900-04-03'),
('OurPlayer12', 2232, 'demo@task5.com', '1900-04-03'),
('Hiii', 2235, 'hiii1@gmail.com', '2004-09-19'),
('Hiii_admin', 2236, 'hiii_admin1@gmail.com', '2004-09-19'),
('farhan', 2237, 'farhan@gmail.com', NULL),
('student0', 2239, 'student0@dinewell.com', '2025-04-15'),
('Hiii_user', 2241, 'hiii_admin1@gmail.com', '2004-09-19'),
('student3', 2242, 'student3@dinewell.com', '2025-04-11'),
('council1', 2244, 'council1@dinewell.com', '2025-04-01'),
('yoadmin', 2245, 'yoadmin', '1990-01-01'),
('iv', 2248, 'iv', '1111-11-11'),
('Council', 2259, 'council@dinewell.com', '2003-04-05'),
('employee1', 2260, 'employee1@dinewell.com', '2003-04-05'),
('Student1', 2264, 'student1@dinewell.com', '2003-04-05'),
('seemaupadhyay@example.com', 2266, 'seemaupadhyay', NULL),
('kunaldevgan@example.com', 2267, 'kunaldevgan', NULL),
('sumitvij@example.com', 2268, 'sumitvij', NULL),
('drishti', 24210033, '24210033@iitgn.ac.in', '2000-01-01'),
('krishan', 24210057, '24210057@iitgn.ac.in', '2000-01-01'),
('shashwat', 24210093, '24210093@example.com', '2000-01-01'),
('KDot', 24210094, 'compton@gmail.com', '1987-06-17'),
('pa', 24210098, 'pa@gmail.com', '2025-04-02'),
('MSP', 24210099, 'mitsanpat@gmail.com', '2004-10-10'),
('Random1', 24210101, 'random1@gmail.com', '2005-10-10'),
('PG', 24210109, 'pg@gmail.com', '1111-11-11'),
('JiyaDesaiNew', 24210111, 'jiyadesai@email.com', '2004-12-14'),
('rajkamal', 24210112, 'raj@123', NULL),
('admin24210057', 24210115, 'admin24210057@gmail.com', NULL),
('notnew', 24210117, 'not.new@example.com', '2000-01-01'),
('sryidk', 24210118, 'sry.idk@example.com', '2000-01-01'),
('imadmin', 24210119, 'imadmin', '1990-01-01'),
('Hiii_admin2', 24210120, 'hiii_admin12@gmail.com', '2004-09-19'),
('imadmin2', 24210122, 'imadmin2', '1990-01-01'),
('SM', 24210124, 'SM@gmail.com', NULL),
('SG', 24210126, 'SG@gmail.com', NULL),
('Temporary', 24210127, 'temp@temp.com', NULL),
('goud3', 24210128, 'goud@gmail.com', NULL),
('brave', 24210130, 'brave.doe@example.com', '1995-06-15'),
('Student2', 24210132, 'student2@dinewell.com', '2003-04-05'),
('imnew', 24210133, 'imnew', '1111-12-12'),
('PSS', 24210134, 'PSS@gmail.com', NULL),
('HSS', 24210137, 'HSS@gmail.com', NULL),
('nayauser', 24210140, 'nayauser', '1111-11-11'),
('manager_4', 24210143, 'manager_4@example.com', '1990-01-01'),
('manager_5', 24210144, 'manager_5@example.com', '1990-01-01'),
('manager_6', 24210145, 'manager_6@example.com', '1990-01-01'),
('adm@123', 24210146, 'kal@123', NULL),
('Hiii_admin3', 24210151, 'hiii_admin12@gmail.com', '2004-09-19'),
('su', 24210153, 's@i', NULL),
('Ravi Kumar', 24210154, 'kumar.ravi@iitgn.ac.in', '1990-01-01'),
('si', 24210156, 's@i', NULL),
('skr', 24210157, 's@i', NULL),
('employee2', 24210158, 'employee2@dinewell.com', '2025-04-02'),
('mehta', 24210164, 'mehta@db.com', '2004-07-13'),
('asdasd', 24210166, 'nishitprajapati77@gmail.com', '2331-12-12'),
('nishit3456', 24210167, 'nishitprajapati75@gmail.com', '2004-02-11'),
('nishit987', 24210169, 'nishitprajapati60@gmail.com', '2001-01-11'),
('Anish Jain', 24210170, 'jain.anish@iitgn.ac.in', '1990-01-01'),
('samaram', 24210176, 'rum@123', NULL),
('sairam', 24210177, 'ram@122', NULL),
('Nandkishor kumar', 24210178, 'kishor008@gmail.com', '2002-11-23'),
('aditya', 24210179, 'aditya.mehta@iitgn.ac.in', '2004-07-13'),
('Rowena40', 24210180, 'your.email+fakedata85750@gmail.com', '2024-06-20'),
('Jannie_Turcotte83', 24210181, 'akedata81262@gmail.com', '2025-01-06'),
('Jesus_Crona66', 24210182, 'your.email+fakedata37052@gmail.com', '2024-09-22'),
('Vella.Leuschke', 24210189, 'your.email+fakedata42111@gmail.com', '2024-08-23'),
('Concepcion36', 24210192, 'your.email+fakedata34483@gmail.com', '2026-01-01'),
('Barbara_Miller', 24210194, 'your.email+fakedata14693@gmail.com', '2025-03-21'),
('Kenya_Waelchi', 24210196, 'your.email+fakedata38803@gmail.com', '2024-12-28'),
('Lonzo4', 24210197, 'your.email+fakedata69550@gmail.com', '2024-12-09'),
('24210115', 24210198, '24210115@gmail.com', '2001-12-12'),
('Weldon10', 24210199, 'your.email+fakedata11508@gmail.com', '2026-03-15'),
('Shaina74', 24210201, 'your.email+fakedata86256@gmail.com', '2025-10-08'),
('Nathanael24', 24210202, 'your.email+fakedata94344@gmail.com', '2025-04-07'),
('admin17', 24210203, 'admin17@example.com', '2000-01-01'),
('Thala', 24210204, 'thala07@gmail.com', '1979-07-07'),
('karanmehra@example.com', 24210209, 'karanmehra', NULL),
('24210111', 24210213, '24210111@gmail.com', '2001-02-21'),
('24210114', 24210215, '24210114@gmail.com', '2000-12-11'),
('Saaho', 24210216, 'saaho@123', NULL),
('24210110', 24210218, '24210110@gmail.com', '2003-01-01'),
('Pratham Sharda', 24210219, 'pratham@tower.com', '2004-11-08'),
('prabhas', 24210220, 'pra@123', NULL),
('farroq', 24210221, 'far@123', NULL),
('24210119', 24210223, '24210119@iitgn.ac.in', '2002-12-23'),
('V30004', 24210224, 'anubhavjoshi@gmail.com', NULL),
('S10015', 24210225, 'shahparth@iitgn.ac.in', NULL),
('S10016', 24210226, 'shahaks@iitgn.ac.in', NULL),
('V30005', 24210227, 'anishasingh@gmail.com', NULL),
('S10017', 24210228, 'parasyogi@gmail.com', NULL),
('ST20005', 24210229, 'sameerkulkarani@gmail.com', NULL),
('V30006', 24210230, 'anjaligarg@gmail.com', NULL),
('ST20006', 24210231, 'anirbandasgupta@gmail.com', NULL),
('V30007', 24210232, 'rahulmehra@gmail.com', NULL),
('V30008', 24210233, 'parth@iitgn.ac.inn', NULL),
('ST20007', 24210234, 'raganisingh@gmail.com', NULL),
('ST20008', 24210235, 'rakeshsharma@gmail.com', NULL),
('ST20009', 24210236, 'akhilkhare@gmail.com', NULL),
('V30009', 24210237, 'anjaligarg@gmail.com', NULL),
('piyush', 24210238, 'piyush@gmail.com', NULL),
('man', 24210240, 'man@123', NULL),
('singh', 24210241, 'mrugank.patil@iitgn.ac.in', NULL),
('sujal', 24210242, 'patel', '2002-05-23'),
('Jethru Varshik', 24210243, 'varshik@iitgn.ac.in', NULL),
('Praveen Rathod', 24210245, 'praveen.rathod@iitgn.ac.in', '2004-03-30'),
('student10', 24210246, 'student10@dinewell.com', '2025-04-16'),
('testuser4278', 24210253, 'test4278@example.com', '2000-01-01'),
('S10018', 24210254, 'johndoe@gmail.com', NULL),
('testuser50138', 24210255, 'test50138@example.com', '2000-01-01'),
('Aditya Mehta', 24210259, 'aditya.mehta@email.com', '2000-07-17'),
('man3', 24210260, 'man3@123', NULL),
('PSTorque', 24210262, 'pstorque', '2005-12-12'),
('Nishi Shah', 24210263, 'nishi@email.com', '2005-03-02'),
('Smita', 24210264, 'smita@gmail.com', '1972-05-07'),
('nandini', 24210268, 'nandini.verma@example.com', '1990-06-25'),
('ritu', 24210270, 'ritu.malhotra@example.com', '1993-04-05'),
('AdminG1', 24210271, 'admin@email.com', '2020-04-16'),
('Jiya Desai Final Register', 24210272, 'jiya@email.com', '2004-12-14'),
('jiya14desai', 24210273, 'jiya@email.com', '2004-12-14'),
('Jayesh', 24210274, 'jayesh@gmail.com', '1970-11-07'),
('Manan Chavda', 24210276, '23110078@iitgn.ac.in', '2006-01-18'),
('Atharva ', 24210277, 'a@gmail.com', '1111-11-11'),
('Prajas Kulkarni', 24210278, '23110252@iitgn.ac.in', '2025-04-03'),
('NewUser', 24210279, 'newuser@gmail.com', NULL),
('Chin', 24210280, 'chin@gmail.com', '2004-02-03'),
('TempUser', 24210282, 'tempuser@gmail.com', NULL),
('NewAdmin', 24210284, 'admin@gmail.com', NULL),
('admin23', 24210286, 'hiii_user2@gmail.com', '2004-09-19'),
('Nishit Prajapati', 24210287, 'nishitprajapati777@gmail.com', '2004-09-19'),
('alice123zz', 24210288, 'alice@example.com', '1995-05-21'),
('bob_smithzz', 24210289, 'bob@example.com', '1992-08-13'),
('diana_rosezz', 24210291, 'diana@rose.com', '1998-07-10'),
('ethan_wzz', 24210292, 'ethan@webmail.com', '1990-01-15'),
('fiona89zz', 24210293, 'fiona@mailbox.com', '1993-03-23'),
('georgeKzz', 24210294, 'georgek@gmail.com', '1987-09-05'),
('hannah88zz', 24210295, 'hannah88@site.org', '1994-11-11'),
('ian_devzz', 24210296, 'ian_dev@devmail.com', '1996-04-18'),
('Nishit pra', 24210298, 'huntersganggaming12@gmail.com', '2004-09-19'),
('nishit user', 24210299, 'huntersganggaming13@gmail.com', '2003-01-03'),
('rahul.sharma@example.com', 24210301, 'rahul.sharma@example.com', NULL),
('jane_nishit_sa1', 24210302, 'jane.doe@example.com', '1995-08-20'),
('Kunal Maske ', 24210303, '23110201@iitgn.ac.in', '2025-03-12'),
('sam', 24210304, 'ru@123', NULL),
('shashwatpandey35', 24210305, 'shashwatpandey35@gmail.com', '2000-03-04'),
('faq', 24210306, 'far@123', NULL),
('shashwat35', 24210307, 'shashwat35@ee.com', NULL),
('user234', 24210308, 'hiii_user2@gmail.com', '2004-09-19'),
('anything', 24210310, 'anything@ee.com', '0001-05-04'),
('shashwatt', 24210311, 'shashwatt@ee.com', '0001-05-04'),
('john', 24210312, 'john@gmailm.com', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `TransactionID` int NOT NULL,
  `Sender` varchar(50) NOT NULL,
  `Receiver` varchar(50) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`TransactionID`, `Sender`, `Receiver`, `Date`) VALUES
(111, 'Admin', 'Acme Supplies', '2025-04-10'),
(1111, 'Admin', 'Acme Supplies', '2025-04-10'),
(1234, 'admin', 'vendor', '2025-04-01'),
(12345, 'Admin', 'Acme Supplies', '2025-04-10'),
(123456, 'Admin', 'Acme Supplies', '2025-04-10'),
(456789, 'Admin', 'Ramesh', '2025-04-16'),
(876543, 'Admin', 'BharatHP', '2025-04-16'),
(12345678, 'Admin001', 'ElectricityDept', '2025-04-15'),
(33333333, 'Admin', 'abc', '2025-04-16');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `G1_report_analytics`
--
ALTER TABLE `G1_report_analytics`
  ADD PRIMARY KEY (`Report_ID`);

--
-- Indexes for table `G2_Venue`
--
ALTER TABLE `G2_Venue`
  ADD PRIMARY KEY (`VenueID`);

--
-- Indexes for table `G3_job_desc`
--
ALTER TABLE `G3_job_desc`
  ADD PRIMARY KEY (`Discipline_name`,`Designation`,`Room_number`,`Building`),
  ADD KEY `Designation` (`Designation`),
  ADD KEY `Discipline_name` (`Discipline_name`),
  ADD KEY `Room_number` (`Room_number`),
  ADD KEY `Building` (`Building`);

--
-- Indexes for table `G4_warden`
--
ALTER TABLE `G4_warden`
  ADD PRIMARY KEY (`warden_id`);

--
-- Indexes for table `G5_guesthouses`
--
ALTER TABLE `G5_guesthouses`
  ADD PRIMARY KEY (`guesthouse_name`);

--
-- Indexes for table `G7_placement_statistics`
--
ALTER TABLE `G7_placement_statistics`
  ADD PRIMARY KEY (`department`);

--
-- Indexes for table `G8_DIGITAL_BOOKS`
--
ALTER TABLE `G8_DIGITAL_BOOKS`
  ADD PRIMARY KEY (`Digital_ID`);

--
-- Indexes for table `G9_pdfdocument`
--
ALTER TABLE `G9_pdfdocument`
  ADD PRIMARY KEY (`DocumentID`),
  ADD KEY `OwnerID` (`OwnerID`);

--
-- Indexes for table `G10_items`
--
ALTER TABLE `G10_items`
  ADD PRIMARY KEY (`item_id`);

--
-- Indexes for table `G11_payments`
--
ALTER TABLE `G11_payments`
  ADD PRIMARY KEY (`PaymentID`),
  ADD KEY `OrderID` (`OrderID`);

--
-- Indexes for table `G12_Doctors`
--
ALTER TABLE `G12_Doctors`
  ADD PRIMARY KEY (`DoctorID`),
  ADD UNIQUE KEY `ContactNumber` (`ContactNumber`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Indexes for table `G13_Route`
--
ALTER TABLE `G13_Route`
  ADD PRIMARY KEY (`RouteID`);

--
-- Indexes for table `G14_revenue`
--
ALTER TABLE `G14_revenue`
  ADD PRIMARY KEY (`Month`);

--
-- Indexes for table `G15_alerts`
--
ALTER TABLE `G15_alerts`
  ADD PRIMARY KEY (`alert_id`);

--
-- Indexes for table `G16_scholarship`
--
ALTER TABLE `G16_scholarship`
  ADD PRIMARY KEY (`Funding_ID`);

--
-- Indexes for table `G17_customer`
--
ALTER TABLE `G17_customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `contact` (`contact`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `Login`
--
ALTER TABLE `Login`
  ADD PRIMARY KEY (`MemberID`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `unique_UserName` (`UserName`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`TransactionID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `G1_report_analytics`
--
ALTER TABLE `G1_report_analytics`
  MODIFY `Report_ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `G2_Venue`
--
ALTER TABLE `G2_Venue`
  MODIFY `VenueID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `G4_warden`
--
ALTER TABLE `G4_warden`
  MODIFY `warden_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `G8_DIGITAL_BOOKS`
--
ALTER TABLE `G8_DIGITAL_BOOKS`
  MODIFY `Digital_ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `G9_pdfdocument`
--
ALTER TABLE `G9_pdfdocument`
  MODIFY `DocumentID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `G11_payments`
--
ALTER TABLE `G11_payments`
  MODIFY `PaymentID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `G15_alerts`
--
ALTER TABLE `G15_alerts`
  MODIFY `alert_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24210313;
--
-- Database: `cs432g11`
--
CREATE DATABASE IF NOT EXISTS `cs432g11` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `cs432g11`;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `member_id` int NOT NULL,
  `access_level` enum('SuperAdmin','Moderator') NOT NULL,
  `date_of_joining` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`member_id`, `access_level`, `date_of_joining`) VALUES
(10, 'SuperAdmin', '2025-04-16'),
(149, 'SuperAdmin', '2025-04-16'),
(150, 'SuperAdmin', '2025-04-16'),
(301, 'SuperAdmin', '2025-04-16'),
(302, 'SuperAdmin', '2025-04-16'),
(447, 'SuperAdmin', '2025-04-16'),
(455, 'SuperAdmin', '2025-04-16'),
(1143, 'SuperAdmin', '2025-04-16'),
(1176, 'SuperAdmin', '2025-04-16'),
(1178, 'SuperAdmin', '2025-04-16'),
(1214, 'SuperAdmin', '2025-04-16'),
(1222, 'SuperAdmin', '2025-04-16'),
(1256, 'SuperAdmin', '2025-04-16'),
(1259, 'SuperAdmin', '2025-04-16'),
(1309, 'SuperAdmin', '2025-04-16'),
(1400, 'SuperAdmin', '2025-04-16'),
(1402, 'SuperAdmin', '2025-04-16'),
(1414, 'SuperAdmin', '2025-04-16'),
(2009, 'SuperAdmin', '2025-04-16'),
(2017, 'SuperAdmin', '2025-04-16'),
(2029, 'SuperAdmin', '2025-04-16'),
(2080, 'SuperAdmin', '2025-04-16'),
(2087, 'SuperAdmin', '2025-04-16'),
(2095, 'SuperAdmin', '2025-04-16'),
(2105, 'SuperAdmin', '2025-04-16'),
(2110, 'SuperAdmin', '2025-04-16'),
(2116, 'SuperAdmin', '2025-04-16'),
(2119, 'SuperAdmin', '2025-04-16'),
(2123, 'SuperAdmin', '2025-04-16'),
(2135, 'SuperAdmin', '2025-04-16'),
(2192, 'SuperAdmin', '2025-04-16'),
(2198, 'SuperAdmin', '2025-04-16'),
(2200, 'SuperAdmin', '2025-04-16'),
(2209, 'SuperAdmin', '2025-04-16'),
(2236, 'SuperAdmin', '2025-04-16'),
(2245, 'SuperAdmin', '2025-04-16'),
(24210098, 'SuperAdmin', '2025-04-16'),
(24210099, 'SuperAdmin', '2025-04-16'),
(24210115, 'SuperAdmin', '2025-04-16'),
(24210117, 'SuperAdmin', '2025-04-16'),
(24210119, 'SuperAdmin', '2025-04-16'),
(24210120, 'SuperAdmin', '2025-04-16'),
(24210127, 'SuperAdmin', '2025-04-16'),
(24210154, 'SuperAdmin', '2025-04-16'),
(24210167, 'SuperAdmin', '2025-04-16'),
(24210245, 'SuperAdmin', '2025-04-16'),
(24210271, 'SuperAdmin', '2025-04-16'),
(24210274, 'SuperAdmin', '2025-04-16'),
(24210286, 'SuperAdmin', '2025-04-16'),
(24210287, 'SuperAdmin', '2025-04-16');

-- --------------------------------------------------------

--
-- Table structure for table `change_logs`
--

CREATE TABLE `change_logs` (
  `log_id` int NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `operation` varchar(50) NOT NULL,
  `table_name` varchar(100) NOT NULL,
  `details` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `change_logs`
--

INSERT INTO `change_logs` (`log_id`, `user_id`, `operation`, `table_name`, `details`, `timestamp`) VALUES
(1, '1', 'INSERT', 'member_portfolio', 'Created portfolio for member ID: 2095', '2025-04-15 13:16:59'),
(2, '1', 'INSERT', 'member_portfolio', 'Created portfolio for member ID: 2200', '2025-04-15 13:25:46'),
(3, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2095', '2025-04-15 13:29:49'),
(4, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2095', '2025-04-15 13:30:15'),
(5, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2095', '2025-04-15 13:33:48'),
(6, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2095', '2025-04-15 13:34:03'),
(7, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2095', '2025-04-15 13:36:29'),
(8, '1', 'INSERT', 'member_portfolio', 'Created portfolio for member ID: 2163', '2025-04-15 13:37:37'),
(9, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2200', '2025-04-15 13:42:55'),
(10, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2163', '2025-04-15 16:06:22'),
(11, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2163', '2025-04-15 18:35:10'),
(12, 'SYSTEM', 'INSERT', 'outlet', 'Created new outlet: New Outlet 7', '2025-04-15 23:07:00'),
(13, 'SYSTEM', 'INSERT', 'outlet', 'Created new outlet: New Outlet 8', '2025-04-15 23:16:10'),
(14, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2163', '2025-04-16 04:36:22'),
(15, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2163', '2025-04-16 04:36:33'),
(16, '1', 'UPDATE', 'member_portfolio', 'Updated portfolio for member ID: 2095', '2025-04-16 04:57:57');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feedback_id` int NOT NULL,
  `member_id` int NOT NULL,
  `outlet_id` int NOT NULL,
  `order_id` int DEFAULT NULL,
  `rating` int NOT NULL,
  `comments` text,
  `feedback_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feedback_id`, `member_id`, `outlet_id`, `order_id`, `rating`, `comments`, `feedback_time`) VALUES
(2, 2163, 2, 11, 2, 'dwshbcijxmewla;xmdw', '2025-04-15 18:44:43'),
(3, 1118, 1, NULL, 5, 'Test feedback inserted directly', '2025-04-15 18:46:10'),
(4, 2163, 4, 10, 2, 'hvhubiojpkkbj', '2025-04-15 18:52:24'),
(5, 1118, 3, NULL, 4, 'Test feedback from direct API test script', '2025-04-15 18:52:54'),
(6, 2163, 6, 21, 5, 'uhirdfokcrejdfoc', '2025-04-16 04:56:06');

-- --------------------------------------------------------

--
-- Stand-in structure for view `group11_members`
-- (See below for the actual view)
--
CREATE TABLE `group11_members` (
`email` varchar(200)
,`member_id` int
,`role` varchar(10)
,`username` varchar(50)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `members_view`
-- (See below for the actual view)
--
CREATE TABLE `members_view` (
`DoB` date
,`Email` varchar(200)
,`MemberID` int
,`Name` varchar(50)
);

-- --------------------------------------------------------

--
-- Table structure for table `member_portfolio`
--

CREATE TABLE `member_portfolio` (
  `portfolio_id` int NOT NULL,
  `member_id` int NOT NULL,
  `bio` text,
  `skills` text,
  `achievements` text,
  `last_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `member_portfolio`
--

INSERT INTO `member_portfolio` (`portfolio_id`, `member_id`, `bio`, `skills`, `achievements`, `last_updated`) VALUES
(1, 2095, '', '', '', '2025-04-15 13:16:59'),
(2, 2200, '', '', '', '2025-04-15 13:25:46'),
(3, 2163, '', '', '', '2025-04-15 13:37:37');

-- --------------------------------------------------------

--
-- Stand-in structure for view `member_profiles`
-- (See below for the actual view)
--
CREATE TABLE `member_profiles` (
`achievements` text
,`bio` text
,`date_of_birth` date
,`email` varchar(200)
,`last_updated` timestamp
,`member_id` int
,`role` varchar(10)
,`skills` text
,`username` varchar(50)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `member_roles`
-- (See below for the actual view)
--
CREATE TABLE `member_roles` (
`email` varchar(200)
,`member_id` int
,`name` varchar(50)
,`role` varchar(13)
);

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `menu_id` int NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `available` tinyint(1) DEFAULT '1',
  `outlet_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`menu_id`, `item_name`, `price`, `available`, `outlet_id`) VALUES
(160, 'Chicken Shawarma (7in Roll)', '100.00', 1, 1),
(161, 'Chicken Lollypop (4pcs)', '120.00', 1, 1),
(162, 'Chicken Lollypop (2pcs)', '70.00', 1, 1),
(163, 'Chicken Hakka Noodles (300gm)', '90.00', 1, 1),
(164, 'Chicken Manchurian Noodles (350gm)', '100.00', 1, 1),
(165, 'Chicken Biryani Boneless (300gm)', '140.00', 1, 1),
(166, 'Chicken Biryani Bone (2-Pcs) (300gm)', '70.00', 1, 1),
(167, 'Chicken Fried Rice (250gm)', '70.00', 1, 1),
(168, 'Chicken Sezwan Fried Rice (250gm)', '80.00', 1, 1),
(169, 'Chicken Chilly Dry (5-PCS)', '140.00', 1, 1),
(170, 'Chicken Curry Thali (Chi-Curry, Rice, 4-Chapati)', '130.00', 1, 1),
(171, 'Butter Chicken Thali (Butter Chi, Rice, 4-Chapati)', '150.00', 1, 1),
(172, 'Chinese Combo (1 PCS Lollipop, Chicken Fried Rice, Chicken Noodles)', '140.00', 1, 1),
(173, 'Chicken Curry (3-pcs) (300gm)', '110.00', 1, 1),
(174, 'Butter Chicken Boneless (350gm)', '140.00', 1, 1),
(175, 'Egg Biryani (2-Egg) (250gm)', '65.00', 1, 1),
(176, 'Egg Fried Rice (250gm)', '65.00', 1, 1),
(177, 'Egg Curry / Masala', '60.00', 1, 1),
(178, 'Egg Curry Thali (2-Egg) (Egg Curry, Rice, 4-Chapati)', '90.00', 1, 1),
(179, 'Egg Kheema (2-Egg)', '60.00', 1, 1),
(180, 'Egg Bhurji (2-Egg) (250gm)', '65.00', 1, 1),
(181, 'Boil Egg (2pcs)', '30.00', 1, 1),
(182, 'Masala Omelette', '40.00', 1, 1),
(183, 'Fish Fried (1pcs)', '60.00', 1, 1),
(184, 'Fish Biryani (1pcs)', '100.00', 1, 1),
(185, 'Fish Fried Rice (250gm)', '100.00', 1, 1),
(186, 'Fish Masala (1pcs)', '120.00', 1, 1),
(187, 'Chapati', '7.00', 1, 1),
(188, 'Plain Rice (300gm)', '40.00', 1, 1),
(189, 'Manchow Soup', '35.00', 1, 2),
(190, 'Manchurian Soup', '35.00', 1, 2),
(191, 'Tomato-Basil Soup', '35.00', 1, 2),
(192, 'Lemon-Coriander Soup', '35.00', 1, 2),
(193, 'Veg Manchurian (Gravy/Dry) Half', '45.00', 1, 2),
(194, 'Veg Manchurian (Gravy/Dry) Full', '65.00', 1, 2),
(195, 'Veg Hakka Noodles Half', '45.00', 1, 2),
(196, 'Veg Hakka Noodles Full', '65.00', 1, 2),
(197, 'Manchurian Noodles Half', '45.00', 1, 2),
(198, 'Manchurian Noodles Full', '65.00', 1, 2),
(199, 'Schezwan Noodles Half', '45.00', 1, 2),
(200, 'Schezwan Noodles Full', '65.00', 1, 2),
(201, 'Paneer Chilli', '90.00', 1, 2),
(202, 'Veg Fried Rice Half', '45.00', 1, 2),
(203, 'Veg Fried Rice Full', '65.00', 1, 2),
(204, 'Manchurian Rice Half', '50.00', 1, 2),
(205, 'Manchurian Rice Full', '70.00', 1, 2),
(206, 'Schezwan Rice Half', '50.00', 1, 2),
(207, 'Schezwan Rice Full', '70.00', 1, 2),
(208, 'Spring Roll', '50.00', 1, 2),
(209, 'Dal Fry Half', '50.00', 1, 2),
(210, 'Dal Fry Full', '70.00', 1, 2),
(211, 'Paneer Masala Half', '80.00', 1, 2),
(212, 'Paneer Masala Full', '110.00', 1, 2),
(213, 'Paneer Butter Masala Half', '90.00', 1, 2),
(214, 'Paneer Butter Masala Full', '120.00', 1, 2),
(215, 'Paneer Kali Mirch Half', '110.00', 1, 2),
(216, 'Paneer Kali Mirch Full', '140.00', 1, 2),
(217, 'Kaju-Paneer Mix Masala Half', '110.00', 1, 2),
(218, 'Kaju-Paneer Mix Masala Full', '140.00', 1, 2),
(219, 'Chicken Dana Half', '50.00', 1, 2),
(220, 'Chicken Dana Full', '100.00', 1, 2),
(221, 'Chicken Lollipop (Dry/Gravy)', '90.00', 1, 2),
(222, 'Chicken Chilly Half', '100.00', 1, 2),
(223, 'Chicken Chilly Full', '150.00', 1, 2),
(224, 'Chicken Masala Half', '90.00', 1, 2),
(225, 'Chicken Masala Full', '140.00', 1, 2),
(226, 'Chicken Korma Half', '100.00', 1, 2),
(227, 'Chicken Korma Full', '150.00', 1, 2),
(228, 'Butter Chicken Half', '100.00', 1, 2),
(229, 'Butter Chicken Full', '150.00', 1, 2),
(230, 'Chicken Bhuna Masala Half', '120.00', 1, 2),
(231, 'Chicken Bhuna Masala Full', '170.00', 1, 2),
(232, 'Chicken Kolhapuri Half', '120.00', 1, 2),
(233, 'Chicken Kolhapuri Full', '170.00', 1, 2),
(234, 'Chicken Ghee Roast Half', '130.00', 1, 2),
(235, 'Chicken Ghee Roast Full', '180.00', 1, 2),
(236, 'Afghani Malai Chicken Half', '140.00', 1, 2),
(237, 'Afghani Malai Chicken Full', '190.00', 1, 2),
(238, 'Chicken Soup', '40.00', 1, 2),
(239, 'Chicken Fried Rice Half', '65.00', 1, 2),
(240, 'Chicken Fried Rice Full', '80.00', 1, 2),
(241, 'Chicken Schezwan Rice Half', '65.00', 1, 2),
(242, 'Chicken Schezwan Rice Full', '80.00', 1, 2),
(243, 'Chicken Noodles Half', '65.00', 1, 2),
(244, 'Chicken Noodles Full', '80.00', 1, 2),
(245, 'Chicken Schezwan Noodles Half', '65.00', 1, 2),
(246, 'Chicken Schezwan Noodles Full', '80.00', 1, 2),
(247, 'Chicken Triple Rice (Soup+Omelette+Rice+Noodle)', '85.00', 1, 2),
(248, 'Boiled Egg Half', '12.00', 1, 2),
(249, 'Boiled Egg Full', '20.00', 1, 2),
(250, 'Omelette + 2 Bread Half', '30.00', 1, 2),
(251, 'Omelette + 2 Bread Full', '40.00', 1, 2),
(252, 'Egg Burji + 2 Bread Half', '30.00', 1, 2),
(253, 'Egg Burji + 2 Bread Full', '40.00', 1, 2),
(254, 'Half-Fry + 2 Bread Half', '30.00', 1, 2),
(255, 'Half-Fry + 2 Bread Full', '40.00', 1, 2),
(256, 'Egg Masala (2 eggs)', '65.00', 1, 2),
(257, 'Egg Makhanwala (2 eggs)', '75.00', 1, 2),
(258, 'Egg Fried Rice Half', '50.00', 1, 2),
(259, 'Egg Fried Rice Full', '65.00', 1, 2),
(260, 'Egg Noodles Half', '45.00', 1, 2),
(261, 'Egg Noodles Full', '70.00', 1, 2),
(262, 'Chai (Elaichi Flavour) Small', '10.00', 1, 2),
(263, 'Chai (Elaichi Flavour) Large', '20.00', 1, 2),
(264, 'Special Chai (Chocolate, Almond, Pan, Rose, Vanilla) Small', '15.00', 1, 2),
(265, 'Special Chai (Chocolate, Almond, Pan, Rose, Vanilla) Large', '30.00', 1, 2),
(266, 'Bread', '5.00', 1, 2),
(267, 'Chapati', '10.00', 1, 2),
(268, 'Malabar Paratha', '20.00', 1, 2),
(269, 'Aloo Paratha', '35.00', 1, 2),
(270, 'Cheese Paratha', '40.00', 1, 2),
(271, 'Paneer Paratha', '50.00', 1, 2),
(272, 'Plain Rice', '40.00', 1, 2),
(273, 'Jeera Rice', '50.00', 1, 2),
(274, 'Special Kolhapuri Misal', '50.00', 1, 2),
(275, 'Special Kolhapuri Chicken Plate', '150.00', 1, 2),
(276, 'Vadapav', '20.00', 1, 2),
(277, 'Vada Sambhar', '40.00', 1, 2),
(278, 'Hot Tea (50ml)', '12.00', 1, 3),
(279, 'Hot Tea (100ml)', '24.00', 1, 3),
(280, 'Sugar Free Tea (100ml)', '32.00', 1, 3),
(281, 'Elaichi Tea (100ml)', '32.00', 1, 3),
(282, 'Ginger Tea (100ml)', '32.00', 1, 3),
(283, 'Indian Masala Tea (100ml)', '32.00', 1, 3),
(284, 'Gud Wali Chai (100ml)', '42.00', 1, 3),
(285, 'Lemon Ice Tea (250ml)', '63.00', 1, 3),
(286, 'Blueberry Rose Mint Ice Tea (250ml)', '63.00', 1, 3),
(287, 'Peach Ice Tea (250ml)', '63.00', 1, 3),
(288, 'Black Tea (160ml)', '32.00', 1, 3),
(289, 'Kavo Tea (160ml)', '32.00', 1, 3),
(290, 'Green Tea (160ml)', '32.00', 1, 3),
(291, 'Hot Coffee (100ml)', '30.00', 1, 3),
(292, 'Hot Vanilla Coffee (100ml)', '42.00', 1, 3),
(293, 'Black Coffee (160ml)', '32.00', 1, 3),
(294, 'Cold Coffee (250ml)', '74.00', 1, 3),
(295, 'Cappuccino (250ml)', '79.00', 1, 3),
(296, 'Hazelnut Coffee (250ml)', '79.00', 1, 3),
(297, 'Hot Milk (160ml)', '25.00', 1, 3),
(298, 'Haldi Milk (160ml)', '32.00', 1, 3),
(299, 'Bournvita Hot (160ml)', '42.00', 1, 3),
(300, 'Bournvita Cold (160ml)', '42.00', 1, 3),
(301, 'Hot Chocolate (160ml)', '84.00', 1, 3),
(302, 'Chocolate Milk Shake (250ml)', '74.00', 1, 3),
(303, 'Rose Milk Shake (250ml)', '74.00', 1, 3),
(304, 'Strawberry Milk Shake (250ml)', '74.00', 1, 3),
(305, 'Fruit Punch (250ml)', '37.00', 1, 3),
(306, 'Lemon Ginger (250ml)', '37.00', 1, 3),
(307, 'Mojito (250ml)', '42.00', 1, 3),
(308, 'Poha (125gm)', '25.00', 1, 3),
(309, 'Upma (200gm)', '35.00', 1, 3),
(310, 'Thepla with Pickle (3 pieces)', '30.00', 1, 3),
(311, 'Khichu (250gm)', '35.00', 1, 3),
(312, 'Maskabun (With Butter, 110gm)', '30.00', 1, 3),
(313, 'Jam Bun (110gm)', '35.00', 1, 3),
(314, 'Spicy Bun', '45.00', 1, 3),
(315, 'Veggie Fingers (5 pieces)', '40.00', 1, 3),
(316, 'Cheese Garlic Bread (3 pieces)', '74.00', 1, 3),
(317, 'French Fries (120gm)', '68.00', 1, 3),
(318, 'French Fries-Peri Peri Sprinkle (120gm)', '78.00', 1, 3),
(319, 'French Fries-Deep Cheezy (140gm)', '95.00', 1, 3),
(320, 'Bread Butter (2 slices)', '32.00', 1, 3),
(321, 'Jam Butter (2 slices)', '32.00', 1, 3),
(322, 'Cheese Butter Sandwich (2 slices)', '53.00', 1, 3),
(323, 'Cheese Chutney Sandwich (2 slices)', '63.00', 1, 3),
(324, 'Mexican Cheese Sandwich (2 slices)', '84.00', 1, 3),
(325, 'Tandoori Paneer Sandwich (2 slices)', '84.00', 1, 3),
(326, 'Cheese Chilli Sandwich (2 slices)', '84.00', 1, 3),
(327, 'Peri Peri Sandwich (2 slices)', '84.00', 1, 3),
(328, 'Schezuan Paneer Sandwich (2 slices)', '84.00', 1, 3),
(329, 'Masala Noodles (150gm)', '42.00', 1, 3),
(330, 'Tadka Noodles (200gm)', '53.00', 1, 3),
(331, 'Extra Vegetable', '10.00', 1, 3),
(332, 'Extra Cheese', '25.00', 1, 3),
(333, 'Extra Namkeen', '5.00', 1, 3),
(334, 'Aluminum Foil Wrapping Charge', '5.00', 1, 3),
(335, 'Aloo Puff', '25.00', 1, 3),
(336, 'Chinese Puff', '30.00', 1, 3),
(337, 'Mexican Puff', '30.00', 1, 3),
(338, 'Bred Butter (Regular)', '30.00', 1, 4),
(339, 'Veg Sandwich (Regular)', '50.00', 1, 4),
(340, 'Veg Cheese Sandwich (Regular)', '60.00', 1, 4),
(341, 'Aloo Mutter Sandwich (Regular)', '50.00', 1, 4),
(342, 'Aloo Veg Sandwich', '50.00', 1, 4),
(343, 'Cheese Sandwich (Regular)', '50.00', 1, 4),
(344, 'Cheese Chutney Sandwich (Regular)', '50.00', 1, 4),
(345, 'Butter Jam Sandwich (Regular)', '40.00', 1, 4),
(346, 'Cheese Jam Sandwich (Regular)', '50.00', 1, 4),
(347, 'Chocolate Sandwich (Regular)', '40.00', 1, 4),
(348, 'Cheese Chocolate Sandwich (Regular)', '60.00', 1, 4),
(349, 'Corn Capsicum Sandwich (Grill)', '100.00', 1, 4),
(350, 'Panjabi Tadka Sandwich (Grill)', '100.00', 1, 4),
(351, 'A.S SPL Club Sandwich (Grill)', '110.00', 1, 4),
(352, 'Vada Pav', '30.00', 1, 4),
(353, 'Peri Peri Vada Pav', '40.00', 1, 4),
(354, 'Cheese Vada Pav', '50.00', 1, 4),
(355, 'Maska Bun', '35.00', 1, 4),
(356, 'Jam Maska Bun', '40.00', 1, 4),
(357, 'Chocolate Maska Bun', '40.00', 1, 4),
(358, 'Poha', '30.00', 1, 4),
(359, 'Samosa (1pc)', '25.00', 1, 4),
(360, 'Dalal Street Bhel', '60.00', 1, 4),
(361, 'Cheese Bhel', '70.00', 1, 4),
(362, 'A.S SPL Bhel', '80.00', 1, 4),
(363, 'Bread Butter (Reg)', '25.00', 1, 5),
(364, 'Bread Butter (Grill)', '35.00', 1, 5),
(365, 'Butter Jam (Reg)', '35.00', 1, 5),
(366, 'Butter Jam (Grill)', '45.00', 1, 5),
(367, 'Vegetable Sandwich (Reg)', '30.00', 1, 5),
(368, 'Vegetable Sandwich (Grill)', '45.00', 1, 5),
(369, 'Aloo Matar Sandwich (Reg)', '35.00', 1, 5),
(370, 'Aloo Matar Sandwich (Grill)', '50.00', 1, 5),
(371, 'Veg Cheese Sandwich (Reg)', '50.00', 1, 5),
(372, 'Veg Cheese Sandwich (Grill)', '60.00', 1, 5),
(373, 'Aloo Cheese Sandwich (Reg)', '50.00', 1, 5),
(374, 'Aloo Cheese Sandwich (Grill)', '60.00', 1, 5),
(375, 'Cheese Sandwich (Reg)', '45.00', 1, 5),
(376, 'Cheese Sandwich (Grill)', '55.00', 1, 5),
(377, 'Cheese Chutney Sandwich (Reg)', '50.00', 1, 5),
(378, 'Cheese Chutney Sandwich (Grill)', '60.00', 1, 5),
(379, 'Cheese Jam Sandwich (Reg)', '45.00', 1, 5),
(380, 'Cheese Jam Sandwich (Grill)', '55.00', 1, 5),
(381, 'Chocolate Sandwich (Reg)', '55.00', 1, 5),
(382, 'Chocolate Sandwich (Grill)', '70.00', 1, 5),
(383, 'Mexican Sandwich (Reg)', '55.00', 1, 5),
(384, 'Mexican Sandwich (Grill)', '70.00', 1, 5),
(385, 'Chocolate Cheese Sandwich (Reg)', '60.00', 1, 5),
(386, 'Chocolate Cheese Sandwich (Grill)', '75.00', 1, 5),
(387, 'Three in One Sandwich (Grill)', '80.00', 1, 5),
(388, 'Club Sandwich (Grill)', '100.00', 1, 5),
(389, 'Burger Sandwich (Grill)', '110.00', 1, 5),
(390, 'Junglee Sandwich (Grill)', '100.00', 1, 5),
(391, 'Paneer Sandwich (Grill)', '100.00', 1, 5),
(392, 'Butter Slice (Reg)', '20.00', 1, 5),
(393, 'Butter Slice (Grill)', '30.00', 1, 5),
(394, 'Butter Jam Slice (Reg)', '25.00', 1, 5),
(395, 'Butter Jam Slice (Grill)', '35.00', 1, 5),
(396, 'Jam Sing Sev Slice (Reg)', '30.00', 1, 5),
(397, 'Jam Sing Sev Slice (Grill)', '40.00', 1, 5),
(398, 'Garlic Slice (Reg)', '25.00', 1, 5),
(399, 'Garlic Slice (Grill)', '35.00', 1, 5),
(400, 'Special Slice (Reg)', '30.00', 1, 5),
(401, 'Special Slice (Grill)', '40.00', 1, 5),
(402, 'Chocolate Slice (Reg)', '25.00', 1, 5),
(403, 'Chocolate Slice (Grill)', '35.00', 1, 5),
(404, 'Cheese Jam Slice (Grill)', '35.00', 1, 5),
(405, 'Cheese Slices (Grill)', '35.00', 1, 5),
(406, 'Chocolate Milkshake', '50.00', 1, 5),
(407, 'Butterscotch Milkshake', '50.00', 1, 5),
(408, 'Strawberry Milkshake', '50.00', 1, 5),
(409, 'Mango Milkshake', '50.00', 1, 5),
(410, 'Pineapple Milkshake', '50.00', 1, 5),
(411, 'Salted French Fries (Reg)', '40.00', 1, 5),
(412, 'Salted French Fries (Cheese)', '60.00', 1, 5),
(413, 'Chat Masala French Fries (Reg)', '50.00', 1, 5),
(414, 'Chat Masala French Fries (Cheese)', '70.00', 1, 5),
(415, 'Dabeli (Oil)', '20.00', 1, 5),
(416, 'Dabeli (Butter)', '30.00', 1, 5),
(417, 'Dabeli (Cheese)', '50.00', 1, 5),
(418, 'Vadapav (Oil)', '25.00', 1, 5),
(419, 'Vadapav (Butter)', '35.00', 1, 5),
(420, 'Vadapav (Cheese)', '55.00', 1, 5),
(421, 'Italian Pizza (Reg)', '70.00', 1, 5),
(422, 'Italian Pizza (Cheese)', '90.00', 1, 5),
(423, 'Jain Pizza (Reg)', '70.00', 1, 5),
(424, 'Jain Pizza (Cheese)', '90.00', 1, 5),
(425, 'Coconut Pizza (Reg)', '80.00', 1, 5),
(426, 'Coconut Pizza (Cheese)', '100.00', 1, 5),
(427, 'Margherita Pizza (Reg)', '90.00', 1, 5),
(428, 'Margherita Pizza (Cheese)', '110.00', 1, 5),
(429, 'Cheese Corn Pizza (Cheese)', '110.00', 1, 5),
(430, 'Paneer Pizza (Cheese)', '100.00', 1, 5),
(431, 'Butter Maskabun (Reg)', '30.00', 1, 5),
(432, 'Butter Maskabun (Cheese)', '45.00', 1, 5),
(433, 'Butter Jam Maskabun (Reg)', '35.00', 1, 5),
(434, 'Butter Jam Maskabun (Cheese)', '50.00', 1, 5),
(435, 'Chocolate Maskabun (Reg)', '40.00', 1, 5),
(436, 'Chocolate Maskabun (Cheese)', '60.00', 1, 5),
(437, 'Aloo Tikki Burger (Reg)', '40.00', 1, 5),
(438, 'Aloo Tikki Burger (Cheese)', '55.00', 1, 5),
(439, 'Vegetable Burger (Reg)', '50.00', 1, 5),
(440, 'Vegetable Burger (Cheese)', '65.00', 1, 5),
(441, 'Mexican Burger (Reg)', '60.00', 1, 5),
(442, 'Mexican Burger (Cheese)', '75.00', 1, 5),
(443, 'Maggi (Reg)', '25.00', 1, 5),
(444, 'Maggi (Masala)', '35.00', 1, 5),
(445, 'Maggi (Cheese)', '50.00', 1, 5),
(446, 'Vegetable Maggi (Reg)', '30.00', 1, 5),
(447, 'Vegetable Maggi (Masala)', '45.00', 1, 5),
(448, 'Vegetable Maggi (Cheese)', '60.00', 1, 5),
(449, 'Bread Pakoda', '30.00', 1, 5),
(450, 'Batata Vada (4 Pieces)', '30.00', 1, 5),
(451, 'Poha (Reg)', '25.00', 1, 5),
(452, 'Poha (Cheese)', '40.00', 1, 5),
(453, 'Samosa (1 Piece)', '15.00', 1, 5),
(454, 'Kulladh Tea', '15.00', 1, 5),
(455, 'Kulladh Coffee', '20.00', 1, 5),
(456, 'Thepla (4 pieces) + Dahi', '40.00', 1, 5),
(457, 'Kutchi Bowl (Reg)', '50.00', 1, 5),
(458, 'Kutchi Bowl (Cheese)', '60.00', 1, 5),
(459, 'Pani Puri (6)', '20.00', 1, 6),
(460, 'Sev Puri (6)', '50.00', 1, 6),
(461, 'Bhel Puri', '50.00', 1, 6),
(462, 'Chutney Puri (6)', '60.00', 1, 6),
(463, 'Kachori (2)', '40.00', 1, 6),
(464, 'Samosa (2)', '40.00', 1, 6),
(465, 'Pyaaz Kachori (2)', '50.00', 1, 6),
(466, 'Dahi Puri (6)', '60.00', 1, 6),
(467, 'Samosa Chaat', '70.00', 1, 6),
(468, 'Kachori Chaat', '70.00', 1, 6),
(469, 'Pyaaz Kachori Chaat', '80.00', 1, 6),
(470, 'Raj Kachori', '80.00', 1, 6),
(471, 'Chole Tikki', '80.00', 1, 6),
(472, 'Chole Samosa', '80.00', 1, 6),
(473, 'Dahi Bhalla', '90.00', 1, 6),
(474, 'Ragda Pattice', '90.00', 1, 6),
(475, 'Idli (2 pcs)', '50.00', 1, 6),
(476, 'Medu Vada (2 pcs)', '50.00', 1, 6),
(477, 'Idli Vada Combo', '60.00', 1, 6),
(478, 'Mini Idli (10 pcs)', '70.00', 1, 6),
(479, 'Plain Dosa', '70.00', 1, 6),
(480, 'Butter Dosa', '80.00', 1, 6),
(481, 'Masala Dosa', '90.00', 1, 6),
(482, 'Butter Masala Dosa', '100.00', 1, 6),
(483, 'Mysore Masala Dosa', '110.00', 1, 6),
(484, 'Cheese Masala Dosa', '120.00', 1, 6),
(485, 'Onion Uttapam', '90.00', 1, 6),
(486, 'Tomato Uttapam', '90.00', 1, 6),
(487, 'Cheese Uttapam', '120.00', 1, 6),
(488, 'Podi Dosa', '100.00', 1, 6),
(489, 'Idli Sambar', '70.00', 1, 6),
(490, 'Vada Sambar', '70.00', 1, 6),
(491, 'Dosa Combo (Plain + Masala)', '150.00', 1, 6),
(492, 'Uttapam Combo (Onion + Tomato)', '150.00', 1, 6),
(493, 'Filter Coffee', '30.00', 1, 6),
(494, 'Masala Tea', '30.00', 1, 6),
(495, 'Lassi (Sweet)', '50.00', 1, 6),
(496, 'Lassi (Salted)', '50.00', 1, 6),
(497, 'Buttermilk', '40.00', 1, 6),
(498, 'Jal Jeera', '40.00', 1, 6);

-- --------------------------------------------------------

--
-- Stand-in structure for view `menu_with_outlet`
-- (See below for the actual view)
--
CREATE TABLE `menu_with_outlet` (
`available` tinyint(1)
,`item_name` varchar(100)
,`menu_id` int
,`outlet_id` int
,`outlet_location` varchar(255)
,`outlet_name` varchar(100)
,`price` decimal(10,2)
);

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

-- --------------------------------------------------------

--
-- Stand-in structure for view `order_details`
-- (See below for the actual view)
--
CREATE TABLE `order_details` (
`customer_name` varchar(50)
,`member_id` int
,`order_id` int
,`order_status` enum('Pending','Completed','Cancelled')
,`order_time` timestamp
,`outlet_id` int
,`outlet_name` varchar(100)
,`total_amount` decimal(10,2)
);

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE `order_items` (
  `order_item_id` int NOT NULL,
  `order_id` int NOT NULL,
  `menu_id` int NOT NULL,
  `quantity` int NOT NULL,
  `subtotal` decimal(10,2) NOT NULL
) ;

--
-- Dumping data for table `order_items`
--

INSERT INTO `order_items` (`order_item_id`, `order_id`, `menu_id`, `quantity`, `subtotal`) VALUES
(1, 1, 160, 1, '100.00'),
(2, 1, 161, 1, '120.00'),
(3, 1, 162, 1, '70.00'),
(4, 2, 160, 1, '100.00'),
(5, 2, 161, 1, '120.00'),
(6, 2, 162, 1, '70.00'),
(7, 3, 160, 2, '200.00'),
(8, 3, 161, 1, '120.00'),
(9, 3, 162, 3, '210.00'),
(10, 4, 189, 2, '70.00'),
(11, 4, 190, 2, '70.00'),
(12, 5, 160, 1, '100.00'),
(13, 5, 161, 1, '120.00'),
(14, 6, 160, 2, '200.00'),
(15, 6, 161, 2, '240.00'),
(16, 7, 495, 1, '50.00'),
(17, 8, 200, 1, '65.00'),
(18, 9, 360, 1, '60.00'),
(19, 10, 355, 1, '35.00'),
(20, 11, 190, 1, '35.00'),
(21, 12, 496, 1, '50.00'),
(22, 13, 384, 1, '70.00'),
(23, 13, 454, 1, '15.00'),
(24, 14, 169, 3, '420.00'),
(25, 15, 362, 3, '240.00'),
(26, 16, 171, 1, '150.00'),
(27, 17, 334, 1, '5.00'),
(28, 18, 160, 1, '100.00'),
(29, 18, 161, 1, '120.00'),
(30, 18, 162, 1, '70.00'),
(31, 19, 160, 1, '100.00'),
(32, 19, 161, 1, '120.00'),
(33, 19, 162, 1, '70.00'),
(34, 20, 426, 1, '100.00'),
(35, 21, 490, 1, '70.00'),
(36, 22, 358, 1, '30.00'),
(37, 23, 228, 1, '100.00'),
(38, 23, 263, 1, '20.00'),
(39, 24, 188, 1, '40.00'),
(40, 25, 352, 1, '30.00'),
(41, 26, 460, 1, '50.00'),
(42, 26, 490, 1, '70.00'),
(43, 27, 362, 1, '80.00'),
(44, 27, 351, 1, '110.00'),
(45, 28, 181, 1, '30.00'),
(46, 28, 174, 1, '140.00'),
(47, 29, 362, 1, '80.00'),
(48, 29, 351, 1, '110.00'),
(49, 30, 181, 1, '30.00'),
(50, 30, 174, 1, '140.00');

-- --------------------------------------------------------

--
-- Table structure for table `outlet`
--

CREATE TABLE `outlet` (
  `outlet_id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `outlet`
--

INSERT INTO `outlet` (`outlet_id`, `name`, `location`) VALUES
(1, 'Dawat', 'H-Hostel, Ground Floor'),
(2, 'Just Chill', 'B-Hostel, Ground Floor'),
(3, 'Tea Post', 'E-Hostel, Ground Floor'),
(4, 'AS FastFood', 'I-Hostel, Ground Floor'),
(5, 'VS Fastfood', 'H-Hostel, Ground Floor'),
(6, 'Madurai Chaat & More', 'Near Sports Complex');

-- --------------------------------------------------------

--
-- Table structure for table `outlet_manager`
--

CREATE TABLE `outlet_manager` (
  `member_id` int NOT NULL,
  `outlet_id` int NOT NULL,
  `auto_assigned` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `outlet_manager`
--

INSERT INTO `outlet_manager` (`member_id`, `outlet_id`, `auto_assigned`) VALUES
(24210238, 4, 0),
(24210241, 1, 0);

-- --------------------------------------------------------

--
-- Stand-in structure for view `payment_details`
-- (See below for the actual view)
--
CREATE TABLE `payment_details` (
`amount_paid` decimal(10,2)
,`customer_name` varchar(50)
,`member_id` int
,`order_id` int
,`payment_id` int
,`payment_method` enum('UPI','Card','Cash')
,`payment_status` enum('Pending','Completed','Failed')
,`payment_time` timestamp
);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int NOT NULL,
  `role_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `role_name`) VALUES
(1, 'admin'),
(2, 'user');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `member_id` int NOT NULL,
  `roll_number` varchar(20) NOT NULL,
  `hostel_name` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`member_id`, `roll_number`, `hostel_name`, `department`) VALUES
(2095, '2211045', 'Hiquom', 'Electrical'),
(2153, 'S2023001', 'H-Hostel', 'Computer Science'),
(2163, '22110158', 'Griwiksh', 'Computer Science and Engineering'),
(2200, '69696', 'Griwiksh', 'Computer Science and Engineering');

-- --------------------------------------------------------

--
-- Table structure for table `user_roles_mapping`
--

CREATE TABLE `user_roles_mapping` (
  `mapping_id` int NOT NULL,
  `member_id` int NOT NULL,
  `role_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure for view `group11_members`
--
DROP TABLE IF EXISTS `group11_members`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cs432g11`@`%` SQL SECURITY DEFINER VIEW `group11_members`  AS SELECT `m`.`ID` AS `member_id`, `m`.`UserName` AS `username`, `m`.`emailID` AS `email`, `l`.`Role` AS `role` FROM ((`cs432cims`.`members` `m` join `cs432cims`.`MemberGroupMapping` `mgm` on((`m`.`ID` = `mgm`.`MemberID`))) join `cs432cims`.`Login` `l` on((`m`.`ID` = `l`.`MemberID`))) WHERE (`mgm`.`GroupID` = 11) ;

-- --------------------------------------------------------

--
-- Structure for view `members_view`
--
DROP TABLE IF EXISTS `members_view`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cs432g11`@`%` SQL SECURITY DEFINER VIEW `members_view`  AS SELECT `cs432cims`.`members`.`ID` AS `MemberID`, `cs432cims`.`members`.`UserName` AS `Name`, ifnull(`cs432cims`.`members`.`emailID`,concat('user',`cs432cims`.`members`.`ID`,'@example.com')) AS `Email`, `cs432cims`.`members`.`DoB` AS `DoB` FROM `cs432cims`.`members` ;

-- --------------------------------------------------------

--
-- Structure for view `member_profiles`
--
DROP TABLE IF EXISTS `member_profiles`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cs432g11`@`%` SQL SECURITY DEFINER VIEW `member_profiles`  AS SELECT `m`.`ID` AS `member_id`, `m`.`UserName` AS `username`, `m`.`emailID` AS `email`, `m`.`DoB` AS `date_of_birth`, `l`.`Role` AS `role`, `mp`.`bio` AS `bio`, `mp`.`skills` AS `skills`, `mp`.`achievements` AS `achievements`, `mp`.`last_updated` AS `last_updated` FROM ((`cs432cims`.`members` `m` left join `cs432cims`.`Login` `l` on((`m`.`ID` = `l`.`MemberID`))) left join `member_portfolio` `mp` on((`m`.`ID` = `mp`.`member_id`))) ;

-- --------------------------------------------------------

--
-- Structure for view `member_roles`
--
DROP TABLE IF EXISTS `member_roles`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cs432g11`@`%` SQL SECURITY DEFINER VIEW `member_roles`  AS SELECT `m`.`ID` AS `member_id`, `m`.`UserName` AS `name`, `m`.`emailID` AS `email`, (case when (`s`.`member_id` is not null) then 'Student' when (`om`.`member_id` is not null) then 'OutletManager' when (`a`.`member_id` is not null) then 'Admin' else 'Unknown' end) AS `role` FROM (((`cs432cims`.`members` `m` left join `student` `s` on((`m`.`ID` = `s`.`member_id`))) left join `outlet_manager` `om` on((`m`.`ID` = `om`.`member_id`))) left join `admin` `a` on((`m`.`ID` = `a`.`member_id`))) ;

-- --------------------------------------------------------

--
-- Structure for view `menu_with_outlet`
--
DROP TABLE IF EXISTS `menu_with_outlet`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cs432g11`@`%` SQL SECURITY DEFINER VIEW `menu_with_outlet`  AS SELECT `m`.`menu_id` AS `menu_id`, `m`.`item_name` AS `item_name`, `m`.`price` AS `price`, `m`.`available` AS `available`, `o`.`outlet_id` AS `outlet_id`, `o`.`name` AS `outlet_name`, `o`.`location` AS `outlet_location` FROM (`menu` `m` join `outlet` `o` on((`m`.`outlet_id` = `o`.`outlet_id`))) ;

-- --------------------------------------------------------

--
-- Structure for view `order_details`
--
DROP TABLE IF EXISTS `order_details`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cs432g11`@`%` SQL SECURITY DEFINER VIEW `order_details`  AS SELECT `o`.`order_id` AS `order_id`, `o`.`member_id` AS `member_id`, `m`.`UserName` AS `customer_name`, `o`.`outlet_id` AS `outlet_id`, `ot`.`name` AS `outlet_name`, `o`.`total_amount` AS `total_amount`, `o`.`order_status` AS `order_status`, `o`.`order_time` AS `order_time` FROM ((`orders` `o` join `cs432cims`.`members` `m` on((`o`.`member_id` = `m`.`ID`))) join `outlet` `ot` on((`o`.`outlet_id` = `ot`.`outlet_id`))) ;

-- --------------------------------------------------------

--
-- Structure for view `payment_details`
--
DROP TABLE IF EXISTS `payment_details`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cs432g11`@`%` SQL SECURITY DEFINER VIEW `payment_details`  AS SELECT `p`.`PaymentID` AS `payment_id`, `p`.`OrderID` AS `order_id`, `p`.`AmountPaid` AS `amount_paid`, `p`.`PaymentMethod` AS `payment_method`, `p`.`PaymentStatus` AS `payment_status`, `p`.`PaymentTime` AS `payment_time`, `o`.`member_id` AS `member_id`, `m`.`UserName` AS `customer_name` FROM ((`cs432cims`.`G11_payments` `p` join `orders` `o` on((`p`.`OrderID` = `o`.`order_id`))) join `cs432cims`.`members` `m` on((`o`.`member_id` = `m`.`ID`))) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`member_id`);

--
-- Indexes for table `change_logs`
--
ALTER TABLE `change_logs`
  ADD PRIMARY KEY (`log_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feedback_id`);

--
-- Indexes for table `member_portfolio`
--
ALTER TABLE `member_portfolio`
  ADD PRIMARY KEY (`portfolio_id`),
  ADD UNIQUE KEY `member_id` (`member_id`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`menu_id`),
  ADD KEY `outlet_id` (`outlet_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `outlet_id` (`outlet_id`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`order_item_id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `menu_id` (`menu_id`);

--
-- Indexes for table `outlet`
--
ALTER TABLE `outlet`
  ADD PRIMARY KEY (`outlet_id`);

--
-- Indexes for table `outlet_manager`
--
ALTER TABLE `outlet_manager`
  ADD PRIMARY KEY (`member_id`),
  ADD KEY `outlet_id` (`outlet_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `role_name` (`role_name`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`member_id`),
  ADD UNIQUE KEY `roll_number` (`roll_number`);

--
-- Indexes for table `user_roles_mapping`
--
ALTER TABLE `user_roles_mapping`
  ADD PRIMARY KEY (`mapping_id`),
  ADD UNIQUE KEY `member_id` (`member_id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `change_logs`
--
ALTER TABLE `change_logs`
  MODIFY `log_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feedback_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `member_portfolio`
--
ALTER TABLE `member_portfolio`
  MODIFY `portfolio_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `menu_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=501;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `order_items`
--
ALTER TABLE `order_items`
  MODIFY `order_item_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `outlet`
--
ALTER TABLE `outlet`
  MODIFY `outlet_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user_roles_mapping`
--
ALTER TABLE `user_roles_mapping`
  MODIFY `mapping_id` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `menu`
--
ALTER TABLE `menu`
  ADD CONSTRAINT `menu_ibfk_1` FOREIGN KEY (`outlet_id`) REFERENCES `outlet` (`outlet_id`) ON DELETE CASCADE;

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`outlet_id`) REFERENCES `outlet` (`outlet_id`) ON DELETE CASCADE;

--
-- Constraints for table `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`menu_id`) ON DELETE CASCADE;

--
-- Constraints for table `outlet_manager`
--
ALTER TABLE `outlet_manager`
  ADD CONSTRAINT `outlet_manager_ibfk_1` FOREIGN KEY (`outlet_id`) REFERENCES `outlet` (`outlet_id`);

--
-- Constraints for table `user_roles_mapping`
--
ALTER TABLE `user_roles_mapping`
  ADD CONSTRAINT `user_roles_mapping_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
