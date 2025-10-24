-- ====================================================================
-- Database : cars_db
-- Purpose  : car_details
-- Author   : Maneesh
-- created  : 24/10/2025
-- ====================================================================

-- creating the database :
CREATE DATABASE IF NOT EXISTS cars_db
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

-- switch to database :
USE cars_db;

-- create table to store the cars data :
CREATE TABLE IF NOT EXISTS cars(
CAR_NAME VARCHAR(20) PRIMARY KEY,
CAR_BRAND VARCHAR(20) NOT NULL,
CAR_MILAGE INT NOT NULL);




