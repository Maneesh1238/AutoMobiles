-- ====================================================================
-- Database : bikes_db
-- Purpose  : bikes_details
-- Author   : Maneesh
-- created  : 22/10/2025
-- ====================================================================

-- creating the database :
CREATE DATABASE IF NOT EXISTS bikes_db
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

-- switch to database :
USE bikes_db;

-- create table to store the cars data :
CREATE TABLE IF NOT EXISTS bikes(
BIKE_NAME VARCHAR(20) PRIMARY KEY,
BIKE_CC VARCHAR(20) NOT NULL,
BIKE_MILEAGE INT NOT NULL );
