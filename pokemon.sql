-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (x86_64)
--
-- Host: localhost    Database: pokemon
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `pokemon_data`
--

DROP TABLE IF EXISTS `pokemon_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokemon_data` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `img_url` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `review` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `user_agent` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokemon_data`
--

LOCK TABLES `pokemon_data` WRITE;
/*!40000 ALTER TABLE `pokemon_data` DISABLE KEYS */;
INSERT INTO `pokemon_data` VALUES (1,'hariyama','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/297.png','water',NULL,NULL,NULL),(2,'porygon','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png','fire',NULL,NULL,NULL),(3,'golduck','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/55.png','water',NULL,NULL,NULL),(4,'magby','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/240.png','fire',NULL,NULL,NULL),(5,'pinsir','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/127.png','water',NULL,NULL,NULL),(6,'ledian','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/166.png','fire',NULL,NULL,NULL),(7,'sceptile','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/254.png','water',NULL,NULL,NULL),(8,'porygon','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png','fire',NULL,NULL,NULL),(9,'pineco','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/204.png','water',NULL,NULL,NULL),(10,'lickitung','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/108.png','fire',NULL,NULL,NULL),(11,'jynx','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/124.png','wind',NULL,NULL,NULL),(12,'hitmontop','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/237.png','earth',NULL,NULL,NULL),(13,'raichu','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png','wind',NULL,NULL,NULL),(14,'houndour','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/228.png','earth',NULL,NULL,NULL),(15,'unown','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/201.png','wind',NULL,NULL,NULL),(16,'houndoom','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/229.png','earth',NULL,NULL,NULL),(17,'azurill','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/298.png','wind',NULL,NULL,NULL),(18,'sentret','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/161.png','earth',NULL,NULL,NULL),(19,'jynx','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/124.png','wind',NULL,NULL,NULL),(20,'loudred','https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/294.png','earth',NULL,NULL,NULL);
/*!40000 ALTER TABLE `pokemon_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-09 21:38:27
