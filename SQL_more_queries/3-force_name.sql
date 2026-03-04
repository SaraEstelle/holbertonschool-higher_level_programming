-- Script that create the table force_name with id and a NOT NULL name column

-- Create the table force_name if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
