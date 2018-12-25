-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: videos
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `meta`
--

DROP TABLE IF EXISTS `meta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `meta` (
  `id_video` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `date_of_recording` varchar(10) DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `lang` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meta`
--

LOCK TABLES `meta` WRITE;
/*!40000 ALTER TABLE `meta` DISABLE KEYS */;
INSERT INTO `meta` VALUES (1,'How to fix a broken heart','16.12.2018','Florida','Guy Winch','english'),(2,'Как ожидания мешают нам добиваться желаемого','17.12.2018','Florida','Emma Stone','русский'),(3,'Магия пофигизма','18.12.2018','London','Kristina Lee','русский');
/*!40000 ALTER TABLE `meta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mimic`
--

DROP TABLE IF EXISTS `mimic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `mimic` (
  `id_video` int(11) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `text` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mimic`
--

LOCK TABLES `mimic` WRITE;
/*!40000 ALTER TABLE `mimic` DISABLE KEYS */;
INSERT INTO `mimic` VALUES (1,1,'улыбка'),(1,1,'поднятые брови'),(1,3,'сжатые брови'),(1,3,'губы к носу'),(1,4,'поднятые брови'),(1,6,'улыбка'),(1,12,'улыбка'),(1,16,'поднятые брови'),(1,18,'сжатые губы'),(1,19,'поджатый подбородок'),(1,22,'поднятые брови'),(1,23,'сжатые губы'),(1,26,'поднятые брови'),(1,27,'поднятые брови'),(1,29,'сведенные у переносицы брови'),(1,44,'прищуренные глаза'),(1,46,'прищуренные глаза'),(3,20,'поднятые брови'),(3,20,'улыбка'),(3,22,'улыбка'),(3,22,'поднятые брови'),(3,25,'улыбка'),(3,26,'сжатые губы'),(2,4,'улыбка'),(2,15,'улыбка'),(2,22,'улыбка'),(2,26,'улыбка'),(2,28,'улыбка'),(2,32,'улыбка'),(2,36,'улыбка');
/*!40000 ALTER TABLE `mimic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `text`
--

DROP TABLE IF EXISTS `text`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `text` (
  `id_video` int(11) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `text` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `text`
--

LOCK TABLES `text` WRITE;
/*!40000 ALTER TABLE `text` DISABLE KEYS */;
INSERT INTO `text` VALUES (1,1,'six months later'),(1,2,'after a lowly weekend in new England'),(1,3,'Rich made reservation at their favourite romantic restoraunt'),(1,9,'Katie knew he was going to propose'),(1,12,'she could barely contain her exitement'),(1,16,'but Rich did not propose to Katie that night'),(1,18,'he broke up with her'),(1,20,'as deeply as he caried for Katie and he did'),(1,24,'he simply was not in love'),(1,26,'Katie'),(1,27,'was shatted'),(1,28,'her heart was trully broken'),(1,30,'and she now has to take another recover'),(1,34,'but five months after the break up'),(1,36,'Katie still could not stop thinking'),(1,38,'about Rich'),(1,39,'her heart was still very much broken'),(1,43,'the question is'),(1,44,'why'),(1,46,'why was this incredebly strong and fantastic woman'),(1,49,'unable to marshall the same emotional resources'),(1,52,'that got her through four years of cancer treatment'),(3,1,'Задачи, события, обязательства'),(3,3,'Отношения'),(3,5,'и выбросить все это на свалку'),(3,6,'без всякого сожаления'),(3,7,'и благодаря этому'),(3,10,'меть возможность посвящать свое время'),(3,12,'силы и деньги тому'),(3,14,'что действительно делает нас счастливыми'),(3,17,'я поняла как это сделать'),(3,19,'это замечательно'),(3,20,'и я называю это'),(3,22,'магией пофигизма'),(3,23,'которая меняет жизнь'),(2,1,'Ваши желания'),(2,2,'и ваши ожидания - это абсолютно разные вещи'),(2,4,'Ожидания - это вера в то'),(2,6,'Получите ли вы желаемое'),(2,8,'Или нет'),(2,10,'Будучи психологом, изучающим'),(2,12,'как люди создают свое будущее'),(2,14,'я поняла одну вещь'),(2,15,'Ожидания, которые не соответствуют жеданиям'),(2,18,'Это не просто причина почему вы не покупаете лотерейный билет'),(2,22,'Это приина по которой вы хотите получить так много всего'),(2,26,'Но вам это не удается'),(2,29,'Сбросить 3-5 килограммов'),(2,32,'Заполучить-ли работу или девушку мечты'),(2,36,'Это причина по которой несмотря на все попытки и зменить ситуацию'),(2,41,'Все останется по-прежнему');
/*!40000 ALTER TABLE `text` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhest`
--

DROP TABLE IF EXISTS `zhest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `zhest` (
  `id_video` int(11) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `zhesticulation` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhest`
--

LOCK TABLES `zhest` WRITE;
/*!40000 ALTER TABLE `zhest` DISABLE KEYS */;
INSERT INTO `zhest` VALUES (1,1,'раскрытие ладоней к зрителям'),(1,2,'движение руками вверх-вниз'),(1,3,'движение руками вниз'),(1,4,'расставленные пальцы'),(1,6,'движение ладонями вверх'),(1,9,'сжатие ладоней'),(1,21,'покачивание головой'),(1,23,'покачивание головой'),(1,29,'сжатие рук в кулаки'),(1,30,'руки в разные стороны'),(1,34,'махание указательным пальцем'),(1,54,'указательный палец вверх'),(3,1,'рука в сторону'),(3,2,'рука в сторону'),(3,3,'руки в сторону'),(3,5,'руки в сторону'),(3,9,'указательный палец вверх'),(3,12,'движение руками вверх-вниз'),(3,15,'руки в стороны'),(3,21,'кивок головой'),(3,22,'круговое движение кистью'),(3,25,'кивок головой'),(2,1,'рука в сторону'),(2,2,'рука в сторону'),(2,3,'скрещенные руки'),(2,4,'руки в сторону'),(2,5,'указательный палец вверх'),(2,11,'вращение кистью'),(2,14,'вращение кистью'),(2,19,'указательный палец в сторону'),(2,26,'указательный палец в сторону'),(2,37,'указательный палец в сторону');
/*!40000 ALTER TABLE `zhest` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-24 21:42:02
