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
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `surv_id` int(11) NOT NULL AUTO_INCREMENT,
  `surv_name` varchar(60) DEFAULT NULL,
  `surv_apartment` varchar(60) DEFAULT NULL,
  `surv_room` varchar(60) DEFAULT NULL,
  `surv_date` date DEFAULT NULL,
  `surv_time` time DEFAULT NULL,
  `surv_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`surv_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES (1,'SRK','1','2','2024-11-05','19:15:53','Detected'),(2,'SRK','1','2','2024-11-05','19:15:55','Detected'),(3,'SRK','1','2','2024-11-05','19:15:56','Detected'),(4,'SRK','1','2','2024-11-05','19:15:58','Detected'),(5,'SRK','1','2','2024-11-05','19:15:53','Detected'),(6,'SRK','1','2','2024-11-05','19:15:55','Detected'),(7,'SRK','1','2','2024-11-05','19:15:56','Detected'),(8,'SRK','1','2','2024-11-05','19:15:58','Detected'),(9,'MS Dhoni','2','1','2024-11-05','22:27:04','Detected'),(10,'MS Dhoni','2','1','2024-11-05','22:27:06','Detected'),(11,'MS Dhoni','2','1','2024-11-05','22:27:07','Detected'),(12,'MS Dhoni','2','1','2024-11-05','22:27:08','Detected'),(13,'MS Dhoni','2','1','2024-11-05','22:27:09','Detected'),(14,'MS Dhoni','2','1','2024-11-05','22:27:10','Detected'),(15,'MS Dhoni','2','1','2024-11-05','22:27:11','Detected'),(16,'MS Dhoni','2','1','2024-11-05','22:27:12','Detected'),(17,'MS Dhoni','2','1','2024-11-05','22:27:24','Detected'),(18,'MS Dhoni','2','1','2024-11-05','22:27:26','Detected'),(19,'MS Dhoni','2','1','2024-11-05','22:27:27','Detected'),(20,'MS Dhoni','2','1','2024-11-06','23:21:55','Detected'),(21,'MS Dhoni','2','1','2024-11-06','23:21:56','Detected'),(22,'MS Dhoni','2','1','2024-11-06','23:21:57','Detected'),(23,'SRK','1','2','2024-11-06','23:36:42','Detected'),(24,'SRK','1','2','2024-11-06','23:36:43','Detected'),(25,'SRK','1','2','2024-11-06','23:36:44','Detected'),(26,'SRK','1','2','2024-11-06','23:36:45','Detected'),(27,'SRK','1','2','2024-11-06','23:36:46','Detected');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-07  2:44:26
