-- creates database hbtn_0d_usa
-- creates table states inside new DATABASE 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL IDENTITY PRIMARY KEY, name VARCHAR(256) NOT NULL);