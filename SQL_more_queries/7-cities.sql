-- Script that creates the database hbtn_0d_usa and the table cities4

-- Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn-0d_usa;

-- Create the table cities if it does not already exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_cities_state FOREIGN KEY (state_id)
        REFERENCES hbtn_0d_usa.states(id)
) ENGINE=InnoDB;
