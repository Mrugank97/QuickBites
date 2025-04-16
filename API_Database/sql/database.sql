-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 14, 2025 at 04:01 PM
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
('Hospitality', 'Junior Accounts Assistant', '308', 'AB3'),
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
(1, 2122, 'Your maintenance request has been submitted successfully.', '2025-04-14 12:18:12');

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
(2017, 'static\\uploads\\profile_images\\2017_1744629277_dog.jpg'),
(2065, 'C://Users/Konain/Checkinout/static/images/vibhajoshi.jpg'),
(2072, 'C://Users/Konain/Checkinout/static/images/chandanrana.jpg'),
(2088, 'C://Users/Konain/Checkinout/static/images/mohitbhattacharya.jpg'),
(2089, 'C://Users/Konain/Checkinout/static/images/sunilrawat.jpg'),
(2093, 'C://Users/Konain/Checkinout/static/images/dhruvgill.jpg'),
(2097, 'C://Users/Konain/Checkinout/static/images/shilpapatel.jpg'),
(2100, 'C://Users/Konain/Checkinout/static/images/rameshvaidya.jpg'),
(2106, 'C://Users/Konain/Checkinout/static/images/namitavarma.jpg'),
(2114, 'C://Users/Konain/Checkinout/static/images/rekhabhattacharya.jpg'),
(2118, 'C://Users/Konain/Checkinout/static/images/shivanikapoor.jpg');

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
('1176', '0e7517141fb53f21ee439b355b5a1d0a', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMTc2LCJyb2xlIjoiQWRtaW4iLCJleHAiOjE3NDQ3NDY0Mjd9.nei_kpzVF6YPdzjQjBMbJM0R3Wnqu-C0n_eMTbKlesg', 1744746427, 'Admin'),
('1177', 'ad6a280417a0f533d8b670c61667e1a0', NULL, NULL, 'Student'),
('1178', '482c811da5d5b4bc6d497ffa98491e38', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibmV3X3VzZXIiLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NDQ2NDM2NTgsImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjoxMTc4fQ.iYBbexlxrF-5NDI6Lm4GSUwtH6dF_zvNhXkAlS7jzkU', 1744623858, 'admin'),
('1182', 'welcome123', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSGFyc2hpdGgiLCJyb2xlIjoidXNlciIsImV4cCI6MTc0NDYyNTMyMiwiZ3JvdXAiOjEyLCJzZXNzaW9uX2lkIjoiMTE4MiJ9.r0_uYbZkZOEe_XvcqmKrUYA6lH4-y4ByAkXgeXGzEsE', 1744625322, 'user'),
('1185', 'e395ad52224de3d5e7fe38f3cb805946f6272758d572fe8a2190fa11951fcbab', '043dc713-3bfe-4e40-9c45-f7d040fc1534', 1744718485, 'user'),
('1191', 'scrypt:32768:8:1$CxijX5NwLJJEn6fM$a2f774ce38832e827bf0c76705b44a5a5d3f42c46b96d13b2bbaad39269ea11aa87cf9ec6467dbf114ff6365022a3f64c883bcaac00d77da0d722ea90130a660', NULL, NULL, 'Student'),
('1196', '2d4f343fb2bc5702c6b1a1965f6ea5fc', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTE5NiIsImV4cCI6MTc0NDU4NjkwN30.YUo-ns-riIKQ6C8769Hn90Oo3urcZ1bP4BTofS21UCw', 1744567108, 'member'),
('1197', '2c68e1d50809e4ae357bcffe1fc99d2a', 'asdf', 1744568898, 'admin'),
('1198', '1a1dc91c907325c69271ddf0c944bc72', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTE5OCIsImV4cCI6MTc0NDU5MjQwM30.Rh31ucgRE_eiAEjMrID1jSEskVIBe3uNcbT0sEdId64', 1744572604, 'admin'),
('1200', '1a1dc91c907325c69271ddf0c944bc72', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTIwMCIsImV4cCI6MTc0NDU5Mjc3N30.J35FSWjNujXIRox-1znD-VAWw2M-sNz9NUE4zyP98_A', 1744572977, 'member'),
('1214', '1a1dc91c907325c69271ddf0c944bc72', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTIxNCIsImV4cCI6MTc0NDU5NjU4OH0.lJkLS72ex_HB5Rie9ZfzbZzpxIn4uD1G5kAsHqHkBC4', 1744576789, 'admin'),
('1215', '1a1dc91c907325c69271ddf0c944bc72', NULL, NULL, 'member'),
('1216', '1a1dc91c907325c69271ddf0c944bc72', NULL, NULL, 'member'),
('1217', '1a1dc91c907325c69271ddf0c944bc72', NULL, NULL, 'member'),
('1218', '1a1dc91c907325c69271ddf0c944bc72', NULL, NULL, 'member'),
('1219', '1a1dc91c907325c69271ddf0c944bc72', NULL, NULL, 'member'),
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
('1310', 'scrypt:32768:8:1$t687fgjedz2unrdj$40ec5018e670d81bb19e68b67ed087ce6cda175be089b7ee806f36503c5c4ff71f8ab2f8f36a07be0e7e8c519ad89f97852f28902b503d7da37ca1d06e4a7afa', NULL, NULL, 'user'),
('1311', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('1312', '$2b$10$0vKsFeiNsB8o8iwo1rbmAucBjjqb/teGmPt/NFekv0RU8V5AjQD8i', NULL, NULL, 'user'),
('1400', 'admin123', '8aa70ca4-b6d2-4bba-a7f3-875397fa7693', 1744639155, 'admin'),
('1402', '1234', NULL, NULL, 'admin'),
('1407', '$2b$10$/2bfOmC7EGD.ZnC0fL05LeNcjAT2g50K9MDHhN8RDgEI5sKcwFiJO', NULL, NULL, 'user'),
('1408', '3dc1e4c3bc5b2ae63520627ea44df7fd', NULL, NULL, 'student'),
('1411', '$2b$10$hUZ39FsgnZYhFQYkSxYK/u0h4zXSw4WASWQKkPIKzWV075OOwTnjS', NULL, NULL, 'user'),
('1413', '$2b$10$rc0H0wdJFfVhNxsB6V3gDuxTWhzvR1VATfUGG4Udj1c4UIz1tg9i2', NULL, NULL, 'user'),
('1414', 'admin@123', NULL, NULL, 'admin'),
('1415', '1234', NULL, NULL, 'admin'),
('1417', '3dc1e4c3bc5b2ae63520627ea44df7fd', NULL, NULL, 'student'),
('1418', '3dc1e4c3bc5b2ae63520627ea44df7fd', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjE0MTgiLCJSb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDYyOTc4MH0.REz16hg3fw-SXBDzNQQfZp0YHm70UrtpzceQEiO--_E', 1744609980, 'student'),
('1419', 'pbkdf2:sha256:260000$R8MKwfCl3L4aK15C$1f52fe44cec650bb7a6eba7fa927fa9f129d33c2fae4dabeb110068349a7f7e7', '68c911e7-fc7c-4f76-a51f-ce672fb3f527', 1744633814, 'user'),
('1428', 'default123', NULL, NULL, 'member'),
('1430', '$2b$05$DeloX1sX6nFPmwn0zG.MUefr13k4ipEloafhwkaL.b4pOq4Zs7Gxq', NULL, NULL, 'user'),
('1431', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('1435', 'pbkdf2:sha256:260000$BtW3O6JFjove2m5t$b09bb35627c6e4b51f61c2e3490e066b702704f24f0be9594945e15035420b9a', 'c4ecc29a-7f1c-4701-8e39-6c6b39aeaac1', 1744631807, 'user'),
('149', 'admin123', 'c807721b-e8b0-466b-af8d-27c7329a7442', 1744392573, 'admin'),
('150', 'default123', NULL, NULL, 'admin'),
('16', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('160', 'default123', '7c57f941-bba0-4d50-b933-a118b6e4b1f7', 1744641507, 'member'),
('164', 'default123', NULL, NULL, 'member'),
('18', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('19', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('192', 'default123', 'cd18da6a-d970-4122-928b-7d856a9819f3', 1744629483, 'member'),
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
('2017', 'youup', NULL, NULL, 'admin'),
('2018', '1234', NULL, NULL, 'User'),
('2019', '52d9df25355b7a1531231bc7351e3a1bf20dc0950e8777d2c5186fecd264fccf', 'CDpTbeBIiXc2dq5mSQXTSX3Pax57UIiF', 7109830, 'Student'),
('2022', '934b535800b1cba8f96a5d72f72f1611', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIwMjIiLCJSb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDYzMTE3OH0.5nQGGo3_okxrbtqAERn_x-AE0k9ycgELXvfdLUN3LaA', 1744611378, 'student'),
('2023', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2024', '934b535800b1cba8f96a5d72f72f1611', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIwMjQiLCJSb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDYzMTI5MX0.ltY75H2hICm7_5scnusrZqeReOJhtq6N7kdJ9b65B3g', 1744611491, 'student'),
('2025', '$2b$05$Zm4SZV4T10jVm0eZ2.YcS.vpC0t2fzcK2lzQLgN5rJdOyctf9czJC', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjAyNSwidXNlcm5hbWUiOiJuaXNoaXRfY2tucG1oMiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYyNzc2OCwiZXhwIjoxNzQ0NjM0OTY4fQ.O_2B_SydTCe6kjZ6dhD7f0HR_GnaTp6P8Vb5CqKhxes', 1744634968, 'admin'),
('2026', 'd84d34224176f0f54b8abd65f639a547', NULL, NULL, 'user'),
('2027', '5b3ce5529c9b0133387e9a7918d79ce88ae7e9d295fd1620248df3a4471b6101', NULL, NULL, 'user'),
('2028', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2029', 'admin@123', NULL, NULL, 'admin'),
('2030', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2032', '1a1dc91c907325c69271ddf0c944bc72', NULL, NULL, 'member'),
('2034', 'c7d84e0c1e60ef7b3fb55fd86c1a8d0b', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjAzNCIsImV4cCI6MTc0NDYzODk3Nn0.sHMNQCzkfGTqIDxiwRmEKuqaBlt9sAyarGLqntW0TOU', 1744619176, 'member'),
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
('2075', 'kuchbhi', NULL, NULL, 'admin'),
('2076', 'f1399249b123cd9a21c9ca367544cda1', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMDc2LCJyb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDc0Mzc2MH0.6tycF76_LPYSdztm2t0ipFr36AX0t-HfGzHE58ldaG0', 1744743760, 'student'),
('2077', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2078', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2080', 'ce5eceb14ac2bc24de2ad5f533d7d84b160714cb3bb485c94a90fc987cc88984', '706c04f3-a679-4b39-988c-70428e2f051f', 1744722926, 'Admin'),
('2083', 'c7d84e0c1e60ef7b3fb55fd86c1a8d0b', NULL, NULL, 'member'),
('2084', 'scrypt:32768:8:1$iSvYZn9ExWrTvC1Y$867e512a3c4d84d5ae2f61f8bfc179d901a68c5f9c150ebe5f3c3377e1076a13102b53403e857b8dcb5dc29694fc40674ed29036fe20012903ac91778d641cf0', NULL, NULL, 'user'),
('2086', '0d0fd7c6e093f7b804fa0150b875b868', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIwODYiLCJSb2xlIjoidmlzaXRvciIsImV4cCI6MTc0NDY0MDg3M30.oUk5rjqOPLdnBjDMDDo7ORP42M6ziBpNGwAwAmWgRB8', 1744621073, 'visitor'),
('2087', 'justchill', NULL, NULL, 'admin'),
('2089', '088359ebe83359087f4e764564bddb8f7d754e67449933f8c5c86765071400d3', 'EKJgkOKei1zlPXjDDePeLoCPlJjCqMfZ', 6620486, 'Visitor'),
('2092', '789d501ae39fde3817ba4fb0d844352e', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjA5MiIsImV4cCI6MTc0NDY0NTg5OX0.yYdPzVvhecnVJWmZSjypETLEW18BkA66uxhm2FHyutM', 1744626099, 'member'),
('2093', '6baf36a8a335c55e8eef90a4ec964e54d9e5349ec2d6bc395ee88b73ddf05062', 'hIOb9xIkuDyPYxe8NJFSqvwF6qaN9yFk', 6940563, 'Student'),
('2094', '9a281eea0823964dfb2915823c248417', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjA5NCIsImV4cCI6MTc0NDY1ODYyMX0.AFoX4tu4zdLA4IntTe9ZgwR008oax2zvu2uvNHpFBAI', 1744638821, 'member'),
('2095', '1c0f1b3576a0a0c525e47a5b51b5723e', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGlwZXNoIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzQ0NjYyMDk2LCJncm91cCI6bnVsbCwic2Vzc2lvbl9pZCI6MjA5NX0.YBLuDs_rha1gnVOCPc9t3CG9mg3GjzqBB_8finoLjug', 1744642297, 'admin'),
('2096', '$2b$05$spwyXWTh7VPpW4MPTrQJA.34ZJTREC1pAkXeG49cLXN4fkDBFWX0a', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjA5NiwidXNlcm5hbWUiOiJLZW5kcmljayBMYW1hciIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYzNzk0NCwiZXhwIjoxNzQ0NjQ1MTQ0fQ.skOkl6deqhiptEVx64_1DGNPoyiki-ylzakiVcJ_w40', 1744645144, 'admin'),
('2099', '$2b$05$4KNauc4/FbhBPS.4/qTHy.uzVJ/7KOFCEwfl4XKB4IgzJG2sifGC6', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjA5OSwidXNlcm5hbWUiOiJLRG90Iiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzQ0NjM4MDQ4LCJleHAiOjE3NDQ2NDUyNDh9.770-UPFYRDIBJV1VNI6NR8N7nKlVFKoRB16owijQ1ec', 1744645248, 'admin'),
('2100', '9936473fc3e4214cc50ee3fc234ba9928a2b86a8617aeeb4b70ee0b47a80b5c7', 'TX9nlCU9PHnz1acpHVrl4aIeavgMO9rZ', 8746809, 'Student'),
('2102', '$2b$05$4DRaWOHHVWV9aqv0ZKwjU.hgzg8NWPlT9XPCJjLpaeprIAyyTkLI2', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjEwMiwidXNlcm5hbWUiOiJLRG90MSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYzODI0OSwiZXhwIjoxNzQ0NjQ1NDQ5fQ.yFgWTGgDJWWq27jX_yL8BOz6yL6na-1xN0aTXUmNJ5o', 1744645449, 'admin'),
('2103', '$2b$05$1MTpxlquO5dF9NLh9ovcoeS0lXltNErwVsQNwINJVqzx1GpNuQa/q', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjEwMywidXNlcm5hbWUiOiJLZW5MYSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYzODQyMSwiZXhwIjoxNzQ0NjQ1NjIxfQ.RBFPPpaX3uVVf5LE-dY46Nk9u9wwmVbQe1YvbRj0Pr0', 1744645621, 'admin'),
('2104', '9f763f085bc07e79baaf4768979e6ee6', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjEwNCIsImV4cCI6MTc0NDYzNzA1N30.MbuqZjAzZbzcKVbz-eJOMSjZFQdh9CU4GBuEdmd49GQ', 1744617258, 'member'),
('2105', '$2b$05$Jg67do5MRVcQOuiOu4BOx.DDNj0OPOMajTD6pGNmebQI28b3joaZS', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjEwNSwidXNlcm5hbWUiOiJQZXJzb24xMiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDYzODUzNSwiZXhwIjoxNzQ0NjQ1NzM1fQ.FIHZw0CX89Zj2dg_oviTdfsGJwmN1d1s00KLhTxZ_qk', 1744645735, 'admin'),
('2109', '808b832900747dfa6be29fe95c4a91e3', NULL, NULL, 'member'),
('2110', '3a5ba419d10b152d73e755e67246eaffd9929711f2e43bc07d37bb7fec6a9c26', NULL, NULL, 'admin'),
('2111', '99a631372a83ff261eae05acb04eb34ba05cf5d8dd3596e1648c5546c0ae18f8', NULL, NULL, 'Chef'),
('2112', '1de12e47f50f37ed7be86e8a06fb6cab', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjExMiIsImV4cCI6MTc0NDYzNzQ3NH0.HynGDH4Ibm0BxKXEWiLMa7hyCU7g_lsSfPGmx2FZnt0', 1744617674, 'member'),
('2113', '2be9bd7a3434f7038ca27d1918de58bd', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIxMTMiLCJSb2xlIjoidmlzaXRvciIsImV4cCI6MTc0NDY0MjYzN30.zEt0M2N7uKv9D2SHYCqm6aqI1elD-sOLNOfexExjcPk', 1744622837, 'visitor'),
('2115', '7d5c009e4eb8bbc78647caeca308e61b', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjExNSIsImV4cCI6MTc0NDY0Mjc2NH0.ZRTH8wVXAawST6bmdI4NXVuh_u8O849iDLF66omzNr4', 1744622964, 'member'),
('2116', '$2b$05$//UVEAnQ7ezJMyviS7vDLODqyeQeIBJsL0hRwLOhvEhe1tp2am7tC', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MjExNiwidXNlcm5hbWUiOiJLZW5kcmlrTGFtYXIiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2MzkzNDAsImV4cCI6MTc0NDY0NjU0MH0.9A4l-Yq1z3Of9xUwfnizaQmLg8x4st8PodEaFRbKQYM', 1744646540, 'admin'),
('2117', 'e9335e177b288c7af4af8f1225c3f938', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0NDciLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2Mzk1NjcsImV4cCI6MTc0NDY0MzE2N30.1t1J5xo5Yjn-6k5v3AThl_69assHuY5HesPFGsqg918', 10800, 'player'),
('2119', '6627415e807ee33c7302917216e7da68', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVlcCIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0NDY1MjM0MywiZ3JvdXAiOiIxIiwic2Vzc2lvbl9pZCI6MjExOX0.wHKSOpqrJdTrZiZtAZa1gv-JHREmcP2Nl3ykKZIKzoc', 1744632543, 'admin'),
('2120', '9f7183e53cc36671b76ae5301b69022c', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVlcC0xIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzQ0NjQ0MDkzLCJncm91cCI6bnVsbCwic2Vzc2lvbl9pZCI6MjEyMH0.mdX-a6OXfNJnneodTXFA-pdBC1ww_J9KdaeJiMlQsdA', 1744624293, 'admin'),
('2121', '449f38c05beb776f9ffffa96f423a922', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVlcC0yIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzQ0NjQ0MjY5LCJncm91cCI6bnVsbCwic2Vzc2lvbl9pZCI6MjEyMX0.utwqJ3yVb83nvEgdEJCMgvZrg-SkIHuAnSXQa0XtedM', 1744624469, 'admin'),
('2122', '006d2143154327a64d86a264aea225f3', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiVnJhaiIsInJvbGUiOiJtZW1iZXIiLCJleHAiOjE3NDQ2NjA3OTQsImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjoyMTIyfQ.cFk59IBRtrLu424u42mu2rK9QTCn3efK2VPeQYTwHb8', 1744640994, 'member'),
('2123', '1234', NULL, NULL, 'admin'),
('2124', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('2125', 'scrypt:32768:8:1$2rFt30KGkdyokrPI$3150146136d0f04b61d9bb042702341d8f641aed529f1c519069fd3c71a4b4db330957d269b99bc34f72d9d737e3e7cd3afd448a72c4944df9172ecc6c17db6a', NULL, NULL, 'Student'),
('2126', '1234', NULL, NULL, 'admin'),
('2127', 'fb6ee30ee24a5ba45c6422e1c6ab5f91', NULL, NULL, 'user'),
('2128', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('2135', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('2136', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'User'),
('2138', 'scrypt:32768:8:1$rseckLwl5dNahSfI$6e3c041cc24361f09967f4ce2100859596bcc5eb4fb5f22d47fc80b5c2e62c54d507db8dbd3deba2ae36069b8fe9d1664a2cfee2ca080d013880767814422353', NULL, NULL, 'Student'),
('2141', '$2b$05$P/I4VI0Nv42lMN4HW6zw6eCTOver/VCya5bMy97EomrroLmXqVRV.', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjIxNDEiLCJ1c2VybmFtZSI6Im5pc2hpdF9ja25wbWgyMyIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc0NDY1OTEwNywiZXhwIjoxNzQ0NjYyNzA3fQ.8PuotBrnggPYGrTYLRcLPL74AJ2cYikhllkvyAkDDqg', 1744662707, 'admin'),
('2142', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('2143', '482c811da5d5b4bc6d497ffa98491e38', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjE0MyIsImV4cCI6MTc0NDY1MjYzOX0.iQY6U_38Rfit3jg5mlscU0LIKcKpo6Qo5BN1aLfzopA', 1744632840, 'member'),
('2144', 'e9335e177b288c7af4af8f1225c3f938', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0NDciLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDQ2NTQxMTcsImV4cCI6MTc0NDY1NzcxN30.g-5mmDF0wAnyjMJ04G1bWjcOlkHMV4VKk_w0KK8ZuTQ', 10800, 'player'),
('2145', '0d0fd7c6e093f7b804fa0150b875b868', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIxNDUiLCJSb2xlIjoidmlzaXRvciIsImV4cCI6MTc0NDY1NzkxOX0.dpMX6HF7TXzwuIUMyCfaNmPwGJdO7mr3fInH7fRPISg', 1744638119, 'visitor'),
('2146', 'f0b53b2da041fca49ef0b9839060b345', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjE0NiIsImV4cCI6MTc0NDY2NDQxN30.OjZZR0KEwWcnXSlYu2GjZOeUp6CWVCKEiqSck9-lhkM', 1744644618, 'member'),
('2148', 'f673d9991a246dbce15d315e7716bc1f', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6IjIxNDgiLCJSb2xlIjoid2FyZGVuIiwiZXhwIjoxNzQ0NjYyMTA1fQ.GFhmDw9i_--l_1BiAGvttdRobnQhWXTODadLMu6HPXc', 1744662105, 'warden'),
('2149', 'defaultPassword', NULL, NULL, 'user'),
('2150', '006d2143154327a64d86a264aea225f3', NULL, NULL, 'student'),
('2151', '006d2143154327a64d86a264aea225f3', NULL, NULL, 'technician'),
('2152', '006d2143154327a64d86a264aea225f3', NULL, NULL, 'admin'),
('2153', '201e8594887c1ef2d551c2a9e582b83b', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMTUzLCJyb2xlIjoic3R1ZGVudCIsImV4cCI6MTc0NDc0NDg0MX0.GYMbVGf_WzY1KysLZGORTrnv3muKG611mhMpChWhxVU', 1744744841, 'student'),
('2154', '006d2143154327a64d86a264aea225f3', NULL, NULL, 'student'),
('2157', '006d2143154327a64d86a264aea225f3', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiVnJhaiBTaGFoIiwicm9sZSI6InN0dWRlbnQiLCJleHAiOjE3NDQ2NjQyNzQsImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjoyMTU3fQ.8Y_AnG1lvdKIygyDVC_ujAAfnY0vQsrMeabDTwjaqyo', 1744644474, 'student'),
('2158', 'd41a22c0780aba6b35efa1b768880f55', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjE1OCIsImV4cCI6MTc0NDY1ODg3MX0.1ClhA-d1ytUqMK8sNgkSgncu-eLtThfmpdNQ3mxlTWE', 1744639071, 'member'),
('2160', 'e9335e177b288c7af4af8f1225c3f938', NULL, NULL, 'user'),
('23', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('24', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('25', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('26', '81dc9bdb52d04dc20036dbd8313ed055', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZW1iZXJfaWQiOiIyNiIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0NDQ4OTYyNC4wNjYwNzZ9.2SeWL-V1JePULL9WG1Xy-2AedcLxVB9AcakoBqQpff0', 1744489624, 'admin'),
('301', 'admin123', '395f2ca9-8c0d-44fc-822b-3922425b8662', 1744641205, 'admin'),
('302', 'admin123', 'd0aadb76-1b61-498d-b2dc-0d224d5eac73', 1744316933, 'admin'),
('31', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('35', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('36', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('38', '81dc9bdb52d04dc20036dbd8313ed055', NULL, NULL, 'admin'),
('424', 'dbsdfugwsifw', NULL, 1756680, 'user'),
('446', '10edeabdb95b0d238cefc8cac7c383af', '', NULL, 'student'),
('447', '1234', NULL, NULL, 'admin'),
('450', '161ebd7d45089b3446ee4e0d86dbcf92', NULL, NULL, 'member'),
('455', 'e4b4efd20ada72c6f7708b0c1cc78469', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdHVzZXIxMjMiLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NDQ2NjEzOTIsImdyb3VwIjpudWxsLCJzZXNzaW9uX2lkIjo0NTV9.Fa-jk7hwtRhr22CXYyQmkytb6urS4Sf0CCqvE7gL0YE', 1744641593, 'admin'),
('456', '5627e974f66a9f51e41799a221120d9ec61af71b7af2d57cf98b8d30d2765f3c', '1ZjivgbwuEaKh2vL17cr0t4eustzs4yR', 8828715, 'Visitor'),
('457', '$2b$05$18.EghoP73pm/xdlP8XpX.lr5M07HR9NyOvdVo3pW8fjDB3Yxtmre', NULL, NULL, 'user'),
('49', '$2b$05$lJ2mBaoyVByqhr6Bz2iqdeIqw1Jw2pRRsrVtIaMPcX8cl1iOhk2EK', NULL, NULL, 'user'),
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
(1215, 1),
(1216, 1),
(1217, 1),
(1218, 1),
(1219, 1),
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
(2032, 1),
(2034, 1),
(2035, 1),
(2038, 1),
(2029, 7),
(164, 15),
(2049, 8),
(2056, 8),
(2065, 5),
(2072, 5),
(2075, 13),
(2076, 14),
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
(2143, 1),
(2146, 1),
(2149, 15),
(2153, 14),
(2158, 1);

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
('Praveen', 2, 'praveen.rathod@iitgn.ac.in', '1990-05-15'),
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
('temp24', 20, 'john.doe@example.com', '1990-05-15'),
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
('aryan', 1415, 'aryan@gmail.com', NULL),
('242100572', 1417, '242100572@iitgn.ac.in', '2001-07-14'),
('242100573', 1418, '242100573@iitgn.ac.in', '2001-07-14'),
('adil', 1419, 'adil@gmail.com', '2025-04-02'),
('Paresh', 1428, 'paresh@gmail.com', '2025-04-10'),
('jane_nishit', 1430, 'jane.doe@example.com', '1995-08-20'),
('Rocky', 1431, 'rocky@gmail.com', NULL),
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
('nevergonna', 2017, 'give@gmail.com', '2025-05-14'),
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
('testtt', 2032, 'aaaaa', '1990-01-01'),
('nimitt1', 2034, 'nimittnim@gmail.com', '2004-09-20'),
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
('Aditya Mangla', 2075, 'aditya.mangla@iitgn.ac.in', '2003-12-11'),
('student0', 2076, 'student0@example.com', '2001-01-01'),
('avinash1', 2077, 'avinash@123', NULL),
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
('testfortransaction', 2143, 'testuser@example.com', '1990-01-01'),
('iamnewhere', 2144, 'new.here@example.com', '2020-01-01'),
('krish', 2145, 'krish@gmail.com', NULL),
('iv', 2146, 'iv', '1111-11-11'),
('krish111', 2148, 'krish111@hostel.edu', NULL),
('John Doe3', 2149, 'john3@example.com', '1990-01-03'),
('student1', 2153, 'student1@example.com', '2001-01-05'),
('Vraj Shah', 2157, 'vraj.shah@iitgn.ac.in', '2004-11-28'),
('siyapatil', 2158, 'siyapatilemail', '2004-04-30'),
('100', 2160, 'new.curl@example.com', '2003-04-03');

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
  MODIFY `Report_ID` int NOT NULL AUTO_INCREMENT;

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
  MODIFY `PaymentID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `G15_alerts`
--
ALTER TABLE `G15_alerts`
  MODIFY `alert_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2161;
--
-- Database: `cs432g11`
--
CREATE DATABASE IF NOT EXISTS `cs432g11` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `cs432g11`;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int NOT NULL,
  `member_id` int NOT NULL,
  `userid` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `member_id`, `userid`, `password`) VALUES
(1, 1, 'testuser123', 'pXqJ5NYz');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`id`, `name`, `email`) VALUES
(1, 'Test User', 'testuser@example.com');

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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `userid` (`userid`),
  ADD KEY `member_id` (`member_id`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `role_name` (`role_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `login`
--
ALTER TABLE `login`
  ADD CONSTRAINT `login_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
