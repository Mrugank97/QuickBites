-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: quickbites
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `MemberID` int NOT NULL,
  `AccessLevel` enum('SuperAdmin','Moderator') NOT NULL,
  `DateOfJoining` date NOT NULL,
  PRIMARY KEY (`MemberID`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`MemberID`) REFERENCES `member` (`MemberID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `FeedbackID` int NOT NULL AUTO_INCREMENT,
  `MemberID` int NOT NULL,
  `MenuID` int NOT NULL,
  `Rating` int NOT NULL,
  `Comments` text,
  `FeedbackTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`FeedbackID`),
  KEY `MemberID` (`MemberID`),
  KEY `MenuID` (`MenuID`),
  CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`MemberID`) REFERENCES `student` (`MemberID`) ON DELETE CASCADE,
  CONSTRAINT `feedback_ibfk_2` FOREIGN KEY (`MenuID`) REFERENCES `menu` (`MenuID`) ON DELETE CASCADE,
  CONSTRAINT `feedback_chk_1` CHECK ((`Rating` between 1 and 5))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `MemberID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Image` varchar(255) NOT NULL,
  `Age` int NOT NULL,
  `Email` varchar(100) NOT NULL,
  `ContactNumber` varchar(15) NOT NULL,
  `Role` enum('Student','OutletManager','Admin') NOT NULL,
  `CreatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`MemberID`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `ContactNumber` (`ContactNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `MenuID` int NOT NULL AUTO_INCREMENT,
  `ItemName` varchar(100) NOT NULL,
  `Price` decimal(10,2) NOT NULL,
  `Available` tinyint(1) DEFAULT '1',
  `OutletID` int NOT NULL,
  PRIMARY KEY (`MenuID`),
  KEY `OutletID` (`OutletID`),
  CONSTRAINT `menu_ibfk_1` FOREIGN KEY (`OutletID`) REFERENCES `outlet` (`OutletID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=340 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Chicken Shawarma (7in Roll)',100.00,1,1),(2,'Chicken Lollypop (4pcs)',120.00,1,1),(3,'Chicken Lollypop (2pcs)',70.00,1,1),(4,'Chicken Hakka Noodles (300gm)',90.00,1,1),(5,'Chicken Manchurian Noodles (350gm)',100.00,1,1),(6,'Chicken Biryani Boneless (300gm)',140.00,1,1),(7,'Chicken Biryani Bone (2-Pcs) (300gm)',70.00,1,1),(8,'Chicken Fried Rice (250gm)',70.00,1,1),(9,'Chicken Sezwan Fried Rice (250gm)',80.00,1,1),(10,'Chicken Chilly Dry (5-PCS)',140.00,1,1),(11,'Chicken Curry Thali (Chi-Curry, Rice, 4-Chapati)',130.00,1,1),(12,'Butter Chicken Thali (Butter Chi, Rice, 4-Chapati)',150.00,1,1),(13,'Chinese Combo (1 PCS Lollipop, Chicken Fried Rice, Chicken Noodles)',140.00,1,1),(14,'Chicken Curry (3-pcs) (300gm)',110.00,1,1),(15,'Butter Chicken Boneless (350gm)',140.00,1,1),(16,'Egg Biryani (2-Egg) (250gm)',65.00,1,1),(17,'Egg Fried Rice (250gm)',65.00,1,1),(18,'Egg Curry / Masala',60.00,1,1),(19,'Egg Curry Thali (2-Egg) (Egg Curry, Rice, 4-Chapati)',90.00,1,1),(20,'Egg Kheema (2-Egg)',60.00,1,1),(21,'Egg Bhurji (2-Egg) (250gm)',65.00,1,1),(22,'Boil Egg (2pcs)',30.00,1,1),(23,'Masala Omelette',40.00,1,1),(24,'Fish Fried (1pcs)',60.00,1,1),(25,'Fish Biryani (1pcs)',100.00,1,1),(26,'Fish Fried Rice (250gm)',100.00,1,1),(27,'Fish Masala (1pcs)',120.00,1,1),(28,'Chapati',7.00,1,1),(29,'Plain Rice (300gm)',40.00,1,1),(30,'Manchow Soup',35.00,1,2),(31,'Manchurian Soup',35.00,1,2),(32,'Tomato-Basil Soup',35.00,1,2),(33,'Lemon-Coriander Soup',35.00,1,2),(34,'Veg Manchurian (Gravy/Dry) Half',45.00,1,2),(35,'Veg Manchurian (Gravy/Dry) Full',65.00,1,2),(36,'Veg Hakka Noodles Half',45.00,1,2),(37,'Veg Hakka Noodles Full',65.00,1,2),(38,'Manchurian Noodles Half',45.00,1,2),(39,'Manchurian Noodles Full',65.00,1,2),(40,'Schezwan Noodles Half',45.00,1,2),(41,'Schezwan Noodles Full',65.00,1,2),(42,'Paneer Chilli',90.00,1,2),(43,'Veg Fried Rice Half',45.00,1,2),(44,'Veg Fried Rice Full',65.00,1,2),(45,'Manchurian Rice Half',50.00,1,2),(46,'Manchurian Rice Full',70.00,1,2),(47,'Schezwan Rice Half',50.00,1,2),(48,'Schezwan Rice Full',70.00,1,2),(49,'Spring Roll',50.00,1,2),(50,'Dal Fry Half',50.00,1,2),(51,'Dal Fry Full',70.00,1,2),(52,'Paneer Masala Half',80.00,1,2),(53,'Paneer Masala Full',110.00,1,2),(54,'Paneer Butter Masala Half',90.00,1,2),(55,'Paneer Butter Masala Full',120.00,1,2),(56,'Paneer Kali Mirch Half',110.00,1,2),(57,'Paneer Kali Mirch Full',140.00,1,2),(58,'Kaju-Paneer Mix Masala Half',110.00,1,2),(59,'Kaju-Paneer Mix Masala Full',140.00,1,2),(60,'Chicken Dana Half',50.00,1,2),(61,'Chicken Dana Full',100.00,1,2),(62,'Chicken Lollipop (Dry/Gravy)',90.00,1,2),(63,'Chicken Chilly Half',100.00,1,2),(64,'Chicken Chilly Full',150.00,1,2),(65,'Chicken Masala Half',90.00,1,2),(66,'Chicken Masala Full',140.00,1,2),(67,'Chicken Korma Half',100.00,1,2),(68,'Chicken Korma Full',150.00,1,2),(69,'Butter Chicken Half',100.00,1,2),(70,'Butter Chicken Full',150.00,1,2),(71,'Chicken Bhuna Masala Half',120.00,1,2),(72,'Chicken Bhuna Masala Full',170.00,1,2),(73,'Chicken Kolhapuri Half',120.00,1,2),(74,'Chicken Kolhapuri Full',170.00,1,2),(75,'Chicken Ghee Roast Half',130.00,1,2),(76,'Chicken Ghee Roast Full',180.00,1,2),(77,'Afghani Malai Chicken Half',140.00,1,2),(78,'Afghani Malai Chicken Full',190.00,1,2),(79,'Chicken Soup',40.00,1,2),(80,'Chicken Fried Rice Half',65.00,1,2),(81,'Chicken Fried Rice Full',80.00,1,2),(82,'Chicken Schezwan Rice Half',65.00,1,2),(83,'Chicken Schezwan Rice Full',80.00,1,2),(84,'Chicken Noodles Half',65.00,1,2),(85,'Chicken Noodles Full',80.00,1,2),(86,'Chicken Schezwan Noodles Half',65.00,1,2),(87,'Chicken Schezwan Noodles Full',80.00,1,2),(88,'Chicken Triple Rice (Soup+Omelette+Rice+Noodle)',85.00,1,2),(89,'Boiled Egg Half',12.00,1,2),(90,'Boiled Egg Full',20.00,1,2),(91,'Omelette + 2 Bread Half',30.00,1,2),(92,'Omelette + 2 Bread Full',40.00,1,2),(93,'Egg Burji + 2 Bread Half',30.00,1,2),(94,'Egg Burji + 2 Bread Full',40.00,1,2),(95,'Half-Fry + 2 Bread Half',30.00,1,2),(96,'Half-Fry + 2 Bread Full',40.00,1,2),(97,'Egg Masala (2 eggs)',65.00,1,2),(98,'Egg Makhanwala (2 eggs)',75.00,1,2),(99,'Egg Fried Rice Half',50.00,1,2),(100,'Egg Fried Rice Full',65.00,1,2),(101,'Egg Noodles Half',45.00,1,2),(102,'Egg Noodles Full',70.00,1,2),(103,'Chai (Elaichi Flavour) Small',10.00,1,2),(104,'Chai (Elaichi Flavour) Large',20.00,1,2),(105,'Special Chai (Chocolate, Almond, Pan, Rose, Vanilla) Small',15.00,1,2),(106,'Special Chai (Chocolate, Almond, Pan, Rose, Vanilla) Large',30.00,1,2),(107,'Bread',5.00,1,2),(108,'Chapati',10.00,1,2),(109,'Malabar Paratha',20.00,1,2),(110,'Aloo Paratha',35.00,1,2),(111,'Cheese Paratha',40.00,1,2),(112,'Paneer Paratha',50.00,1,2),(113,'Plain Rice',40.00,1,2),(114,'Jeera Rice',50.00,1,2),(115,'Special Kolhapuri Misal',50.00,1,2),(116,'Special Kolhapuri Chicken Plate',150.00,1,2),(117,'Vadapav',20.00,1,2),(118,'Vada Sambhar',40.00,1,2),(119,'Hot Tea (50ml)',12.00,1,3),(120,'Hot Tea (100ml)',24.00,1,3),(121,'Sugar Free Tea (100ml)',32.00,1,3),(122,'Elaichi Tea (100ml)',32.00,1,3),(123,'Ginger Tea (100ml)',32.00,1,3),(124,'Indian Masala Tea (100ml)',32.00,1,3),(125,'Gud Wali Chai (100ml)',42.00,1,3),(126,'Lemon Ice Tea (250ml)',63.00,1,3),(127,'Blueberry Rose Mint Ice Tea (250ml)',63.00,1,3),(128,'Peach Ice Tea (250ml)',63.00,1,3),(129,'Black Tea (160ml)',32.00,1,3),(130,'Kavo Tea (160ml)',32.00,1,3),(131,'Green Tea (160ml)',32.00,1,3),(132,'Hot Coffee (100ml)',30.00,1,3),(133,'Hot Vanilla Coffee (100ml)',42.00,1,3),(134,'Black Coffee (160ml)',32.00,1,3),(135,'Cold Coffee (250ml)',74.00,1,3),(136,'Cappuccino (250ml)',79.00,1,3),(137,'Hazelnut Coffee (250ml)',79.00,1,3),(138,'Hot Milk (160ml)',25.00,1,3),(139,'Haldi Milk (160ml)',32.00,1,3),(140,'Bournvita Hot (160ml)',42.00,1,3),(141,'Bournvita Cold (160ml)',42.00,1,3),(142,'Hot Chocolate (160ml)',84.00,1,3),(143,'Chocolate Milk Shake (250ml)',74.00,1,3),(144,'Rose Milk Shake (250ml)',74.00,1,3),(145,'Strawberry Milk Shake (250ml)',74.00,1,3),(146,'Fruit Punch (250ml)',37.00,1,3),(147,'Lemon Ginger (250ml)',37.00,1,3),(148,'Mojito (250ml)',42.00,1,3),(149,'Poha (125gm)',25.00,1,3),(150,'Upma (200gm)',35.00,1,3),(151,'Thepla with Pickle (3 pieces)',30.00,1,3),(152,'Khichu (250gm)',35.00,1,3),(153,'Maskabun (With Butter, 110gm)',30.00,1,3),(154,'Jam Bun (110gm)',35.00,1,3),(155,'Spicy Bun',45.00,1,3),(156,'Veggie Fingers (5 pieces)',40.00,1,3),(157,'Cheese Garlic Bread (3 pieces)',74.00,1,3),(158,'French Fries (120gm)',68.00,1,3),(159,'French Fries-Peri Peri Sprinkle (120gm)',78.00,1,3),(160,'French Fries-Deep Cheezy (140gm)',95.00,1,3),(161,'Bread Butter (2 slices)',32.00,1,3),(162,'Jam Butter (2 slices)',32.00,1,3),(163,'Cheese Butter Sandwich (2 slices)',53.00,1,3),(164,'Cheese Chutney Sandwich (2 slices)',63.00,1,3),(165,'Mexican Cheese Sandwich (2 slices)',84.00,1,3),(166,'Tandoori Paneer Sandwich (2 slices)',84.00,1,3),(167,'Cheese Chilli Sandwich (2 slices)',84.00,1,3),(168,'Peri Peri Sandwich (2 slices)',84.00,1,3),(169,'Schezuan Paneer Sandwich (2 slices)',84.00,1,3),(170,'Masala Noodles (150gm)',42.00,1,3),(171,'Tadka Noodles (200gm)',53.00,1,3),(172,'Extra Vegetable',10.00,1,3),(173,'Extra Cheese',25.00,1,3),(174,'Extra Namkeen',5.00,1,3),(175,'Aluminum Foil Wrapping Charge',5.00,1,3),(176,'Aloo Puff',25.00,1,3),(177,'Chinese Puff',30.00,1,3),(178,'Mexican Puff',30.00,1,3),(179,'Bred Butter (Regular)',30.00,1,4),(180,'Veg Sandwich (Regular)',50.00,1,4),(181,'Veg Cheese Sandwich (Regular)',60.00,1,4),(182,'Aloo Mutter Sandwich (Regular)',50.00,1,4),(183,'Aloo Veg Sandwich',50.00,1,4),(184,'Cheese Sandwich (Regular)',50.00,1,4),(185,'Cheese Chutney Sandwich (Regular)',50.00,1,4),(186,'Butter Jam Sandwich (Regular)',40.00,1,4),(187,'Cheese Jam Sandwich (Regular)',50.00,1,4),(188,'Chocolate Sandwich (Regular)',40.00,1,4),(189,'Cheese Chocolate Sandwich (Regular)',60.00,1,4),(190,'Corn Capsicum Sandwich (Grill)',100.00,1,4),(191,'Panjabi Tadka Sandwich (Grill)',100.00,1,4),(192,'A.S SPL Club Sandwich (Grill)',110.00,1,4),(193,'Vada Pav',30.00,1,4),(194,'Peri Peri Vada Pav',40.00,1,4),(195,'Cheese Vada Pav',50.00,1,4),(196,'Maska Bun',35.00,1,4),(197,'Jam Maska Bun',40.00,1,4),(198,'Chocolate Maska Bun',40.00,1,4),(199,'Poha',30.00,1,4),(200,'Samosa (1pc)',25.00,1,4),(201,'Dalal Street Bhel',60.00,1,4),(202,'Cheese Bhel',70.00,1,4),(203,'A.S SPL Bhel',80.00,1,4),(204,'Bread Butter (Reg)',25.00,1,5),(205,'Bread Butter (Grill)',35.00,1,5),(206,'Butter Jam (Reg)',35.00,1,5),(207,'Butter Jam (Grill)',45.00,1,5),(208,'Vegetable Sandwich (Reg)',30.00,1,5),(209,'Vegetable Sandwich (Grill)',45.00,1,5),(210,'Aloo Matar Sandwich (Reg)',35.00,1,5),(211,'Aloo Matar Sandwich (Grill)',50.00,1,5),(212,'Veg Cheese Sandwich (Reg)',50.00,1,5),(213,'Veg Cheese Sandwich (Grill)',60.00,1,5),(214,'Aloo Cheese Sandwich (Reg)',50.00,1,5),(215,'Aloo Cheese Sandwich (Grill)',60.00,1,5),(216,'Cheese Sandwich (Reg)',45.00,1,5),(217,'Cheese Sandwich (Grill)',55.00,1,5),(218,'Cheese Chutney Sandwich (Reg)',50.00,1,5),(219,'Cheese Chutney Sandwich (Grill)',60.00,1,5),(220,'Cheese Jam Sandwich (Reg)',45.00,1,5),(221,'Cheese Jam Sandwich (Grill)',55.00,1,5),(222,'Chocolate Sandwich (Reg)',55.00,1,5),(223,'Chocolate Sandwich (Grill)',70.00,1,5),(224,'Mexican Sandwich (Reg)',55.00,1,5),(225,'Mexican Sandwich (Grill)',70.00,1,5),(226,'Chocolate Cheese Sandwich (Reg)',60.00,1,5),(227,'Chocolate Cheese Sandwich (Grill)',75.00,1,5),(228,'Three in One Sandwich (Grill)',80.00,1,5),(229,'Club Sandwich (Grill)',100.00,1,5),(230,'Burger Sandwich (Grill)',110.00,1,5),(231,'Junglee Sandwich (Grill)',100.00,1,5),(232,'Paneer Sandwich (Grill)',100.00,1,5),(233,'Butter Slice (Reg)',20.00,1,5),(234,'Butter Slice (Grill)',30.00,1,5),(235,'Butter Jam Slice (Reg)',25.00,1,5),(236,'Butter Jam Slice (Grill)',35.00,1,5),(237,'Jam Sing Sev Slice (Reg)',30.00,1,5),(238,'Jam Sing Sev Slice (Grill)',40.00,1,5),(239,'Garlic Slice (Reg)',25.00,1,5),(240,'Garlic Slice (Grill)',35.00,1,5),(241,'Special Slice (Reg)',30.00,1,5),(242,'Special Slice (Grill)',40.00,1,5),(243,'Chocolate Slice (Reg)',25.00,1,5),(244,'Chocolate Slice (Grill)',35.00,1,5),(245,'Cheese Jam Slice (Grill)',35.00,1,5),(246,'Cheese Slices (Grill)',35.00,1,5),(247,'Chocolate Milkshake',50.00,1,5),(248,'Butterscotch Milkshake',50.00,1,5),(249,'Strawberry Milkshake',50.00,1,5),(250,'Mango Milkshake',50.00,1,5),(251,'Pineapple Milkshake',50.00,1,5),(252,'Salted French Fries (Reg)',40.00,1,5),(253,'Salted French Fries (Cheese)',60.00,1,5),(254,'Chat Masala French Fries (Reg)',50.00,1,5),(255,'Chat Masala French Fries (Cheese)',70.00,1,5),(256,'Dabeli (Oil)',20.00,1,5),(257,'Dabeli (Butter)',30.00,1,5),(258,'Dabeli (Cheese)',50.00,1,5),(259,'Vadapav (Oil)',25.00,1,5),(260,'Vadapav (Butter)',35.00,1,5),(261,'Vadapav (Cheese)',55.00,1,5),(262,'Italian Pizza (Reg)',70.00,1,5),(263,'Italian Pizza (Cheese)',90.00,1,5),(264,'Jain Pizza (Reg)',70.00,1,5),(265,'Jain Pizza (Cheese)',90.00,1,5),(266,'Coconut Pizza (Reg)',80.00,1,5),(267,'Coconut Pizza (Cheese)',100.00,1,5),(268,'Margherita Pizza (Reg)',90.00,1,5),(269,'Margherita Pizza (Cheese)',110.00,1,5),(270,'Cheese Corn Pizza (Cheese)',110.00,1,5),(271,'Paneer Pizza (Cheese)',100.00,1,5),(272,'Butter Maskabun (Reg)',30.00,1,5),(273,'Butter Maskabun (Cheese)',45.00,1,5),(274,'Butter Jam Maskabun (Reg)',35.00,1,5),(275,'Butter Jam Maskabun (Cheese)',50.00,1,5),(276,'Chocolate Maskabun (Reg)',40.00,1,5),(277,'Chocolate Maskabun (Cheese)',60.00,1,5),(278,'Aloo Tikki Burger (Reg)',40.00,1,5),(279,'Aloo Tikki Burger (Cheese)',55.00,1,5),(280,'Vegetable Burger (Reg)',50.00,1,5),(281,'Vegetable Burger (Cheese)',65.00,1,5),(282,'Mexican Burger (Reg)',60.00,1,5),(283,'Mexican Burger (Cheese)',75.00,1,5),(284,'Maggi (Reg)',25.00,1,5),(285,'Maggi (Masala)',35.00,1,5),(286,'Maggi (Cheese)',50.00,1,5),(287,'Vegetable Maggi (Reg)',30.00,1,5),(288,'Vegetable Maggi (Masala)',45.00,1,5),(289,'Vegetable Maggi (Cheese)',60.00,1,5),(290,'Bread Pakoda',30.00,1,5),(291,'Batata Vada (4 Pieces)',30.00,1,5),(292,'Poha (Reg)',25.00,1,5),(293,'Poha (Cheese)',40.00,1,5),(294,'Samosa (1 Piece)',15.00,1,5),(295,'Kulladh Tea',15.00,1,5),(296,'Kulladh Coffee',20.00,1,5),(297,'Thepla (4 pieces) + Dahi',40.00,1,5),(298,'Kutchi Bowl (Reg)',50.00,1,5),(299,'Kutchi Bowl (Cheese)',60.00,1,5),(300,'Pani Puri (6)',20.00,1,6),(301,'Sev Puri (6)',50.00,1,6),(302,'Bhel Puri',50.00,1,6),(303,'Chutney Puri (6)',60.00,1,6),(304,'Kachori (2)',40.00,1,6),(305,'Samosa (2)',40.00,1,6),(306,'Pyaaz Kachori (2)',50.00,1,6),(307,'Dahi Puri (6)',60.00,1,6),(308,'Samosa Chaat',70.00,1,6),(309,'Kachori Chaat',70.00,1,6),(310,'Pyaaz Kachori Chaat',80.00,1,6),(311,'Raj Kachori',80.00,1,6),(312,'Chole Tikki',80.00,1,6),(313,'Chole Samosa',80.00,1,6),(314,'Dahi Bhalla',90.00,1,6),(315,'Ragda Pattice',90.00,1,6),(316,'Idli (2 pcs)',50.00,1,6),(317,'Medu Vada (2 pcs)',50.00,1,6),(318,'Idli Vada Combo',60.00,1,6),(319,'Mini Idli (10 pcs)',70.00,1,6),(320,'Plain Dosa',70.00,1,6),(321,'Butter Dosa',80.00,1,6),(322,'Masala Dosa',90.00,1,6),(323,'Butter Masala Dosa',100.00,1,6),(324,'Mysore Masala Dosa',110.00,1,6),(325,'Cheese Masala Dosa',120.00,1,6),(326,'Onion Uttapam',90.00,1,6),(327,'Tomato Uttapam',90.00,1,6),(328,'Cheese Uttapam',120.00,1,6),(329,'Podi Dosa',100.00,1,6),(330,'Idli Sambar',70.00,1,6),(331,'Vada Sambar',70.00,1,6),(332,'Dosa Combo (Plain + Masala)',150.00,1,6),(333,'Uttapam Combo (Onion + Tomato)',150.00,1,6),(334,'Filter Coffee',30.00,1,6),(335,'Masala Tea',30.00,1,6),(336,'Lassi (Sweet)',50.00,1,6),(337,'Lassi (Salted)',50.00,1,6),(338,'Buttermilk',40.00,1,6),(339,'Jal Jeera',40.00,1,6);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderitems`
--

DROP TABLE IF EXISTS `orderitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderitems` (
  `OrderItemID` int NOT NULL AUTO_INCREMENT,
  `OrderID` int NOT NULL,
  `MenuID` int NOT NULL,
  `Quantity` int NOT NULL,
  `Subtotal` decimal(10,2) NOT NULL,
  PRIMARY KEY (`OrderItemID`),
  KEY `OrderID` (`OrderID`),
  KEY `MenuID` (`MenuID`),
  CONSTRAINT `orderitems_ibfk_1` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`) ON DELETE CASCADE,
  CONSTRAINT `orderitems_ibfk_2` FOREIGN KEY (`MenuID`) REFERENCES `menu` (`MenuID`) ON DELETE CASCADE,
  CONSTRAINT `orderitems_chk_1` CHECK ((`Quantity` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderitems`
--

LOCK TABLES `orderitems` WRITE;
/*!40000 ALTER TABLE `orderitems` DISABLE KEYS */;
/*!40000 ALTER TABLE `orderitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `OrderID` int NOT NULL AUTO_INCREMENT,
  `MemberID` int NOT NULL,
  `OutletID` int NOT NULL,
  `TotalAmount` decimal(10,2) NOT NULL,
  `OrderStatus` enum('Pending','Completed','Cancelled') DEFAULT 'Pending',
  `OrderTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`OrderID`),
  KEY `MemberID` (`MemberID`),
  KEY `OutletID` (`OutletID`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`MemberID`) REFERENCES `student` (`MemberID`) ON DELETE CASCADE,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`OutletID`) REFERENCES `outlet` (`OutletID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outlet`
--

DROP TABLE IF EXISTS `outlet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outlet` (
  `OutletID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Location` varchar(255) NOT NULL,
  PRIMARY KEY (`OutletID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outlet`
--

LOCK TABLES `outlet` WRITE;
/*!40000 ALTER TABLE `outlet` DISABLE KEYS */;
INSERT INTO `outlet` VALUES (1,'Dawat','H-Hostel. Ground Floor'),(2,'Just Chill','B-Hostel, Ground Floor'),(3,'Tea Post','E-Hostel, Ground Floor'),(4,'AS FastFood','I-Hostel, Ground Floor'),(5,'VS Fastfood','H-Hostel, Ground Floor'),(6,'Madurai Chaat & More','Near Sports Complex');
/*!40000 ALTER TABLE `outlet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outletmanager`
--

DROP TABLE IF EXISTS `outletmanager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outletmanager` (
  `MemberID` int NOT NULL,
  `AssignedOutletID` int DEFAULT NULL,
  PRIMARY KEY (`MemberID`),
  UNIQUE KEY `AssignedOutletID` (`AssignedOutletID`),
  CONSTRAINT `outletmanager_ibfk_1` FOREIGN KEY (`MemberID`) REFERENCES `member` (`MemberID`) ON DELETE CASCADE,
  CONSTRAINT `outletmanager_ibfk_2` FOREIGN KEY (`AssignedOutletID`) REFERENCES `outlet` (`OutletID`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outletmanager`
--

LOCK TABLES `outletmanager` WRITE;
/*!40000 ALTER TABLE `outletmanager` DISABLE KEYS */;
/*!40000 ALTER TABLE `outletmanager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `PaymentID` int NOT NULL AUTO_INCREMENT,
  `OrderID` int NOT NULL,
  `AmountPaid` decimal(10,2) NOT NULL,
  `PaymentMethod` enum('UPI','Card','Cash') NOT NULL,
  `PaymentStatus` enum('Pending','Completed','Failed') DEFAULT 'Pending',
  `PaymentTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`PaymentID`),
  KEY `OrderID` (`OrderID`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `MemberID` int NOT NULL,
  `RollNumber` varchar(20) NOT NULL,
  `HostelName` varchar(100) NOT NULL,
  `Department` varchar(100) NOT NULL,
  PRIMARY KEY (`MemberID`),
  UNIQUE KEY `RollNumber` (`RollNumber`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`MemberID`) REFERENCES `member` (`MemberID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-28 22:16:09
