-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema proagro_softfocus
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proagro_softfocus
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proagro_softfocus` ;
USE `proagro_softfocus` ;

-- -----------------------------------------------------
-- Table `proagro_softfocus`.`analysts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proagro_softfocus`.`analysts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(300) NOT NULL,
  `email` VARCHAR(300) NOT NULL,
  `password` VARCHAR(300) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT now(),
  `isSuper` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proagro_softfocus`.`loss_communication`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proagro_softfocus`.`loss_communication` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `analysts_id` INT NOT NULL,
  `farmer_name` VARCHAR(300) NOT NULL,
  `farmer_email` VARCHAR(300) NOT NULL,
  `farmer_document` VARCHAR(20) NOT NULL,
  `location` POINT NOT NULL,
  `harvest_date` DATE NOT NULL DEFAULT (DATE(NOW())),
  `cause_of_loss` ENUM('excessive_rain', 'frost', 'hail', 'dry', 'gale', 'ray') NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT now(),
  `deleted` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  INDEX `fk_loss_communication_analysts_idx` (`analysts_id` ASC) VISIBLE,
  CONSTRAINT `fk_loss_communication_analysts`
    FOREIGN KEY (`analysts_id`)
    REFERENCES `proagro_softfocus`.`analysts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
