-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: sql12.freesqldatabase.com    Database: sql12730185
-- ------------------------------------------------------
-- Server version	5.5.62-0ubuntu0.14.04.1

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
-- Table structure for table `tenant`
--

DROP TABLE IF EXISTS `tenant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tenant` (
  `t_id` int(11) NOT NULL COMMENT 'Unique identifier for each tenant (Primary Key)',
  `t_name` varchar(60) DEFAULT NULL COMMENT 'The name of the tenant',
  `t_phno` varchar(60) DEFAULT NULL COMMENT 'The tenant’s phone number',
  `t_email` varchar(60) DEFAULT NULL COMMENT 'The tenant’s email address',
  `t_apartment` varchar(60) DEFAULT NULL COMMENT 'The apartment building where the tenant resides',
  `t_room` varchar(60) DEFAULT NULL COMMENT 'The tenant’s room or number',
  `t_occupancy_period` varchar(60) DEFAULT NULL COMMENT 'The duration of the tenant''s stay',
  `t_occupancy_number` varchar(60) DEFAULT NULL COMMENT 'The number of occupants in the tenant''s apartment',
  `t_photo_sample` varchar(60) DEFAULT NULL COMMENT 'The tenant’s facial photo sample taken or not for recognition',
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tenant`
--

LOCK TABLES `tenant` WRITE;
/*!40000 ALTER TABLE `tenant` DISABLE KEYS */;
INSERT INTO `tenant` VALUES (1,'SRK','1234567','srk@gmail.com','1','2','2022-23','3','Yes'),(2,'MS Dhoni','134567','msdhoni@gmail.com','2','1','2022-23','1','Yes'),(3,'Akshai','12345678910','akshai@gmail.com','3','2','2025-26','2','Yes');
/*!40000 ALTER TABLE `tenant` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-07  2:45:30
