-- Script that creates the table id_not_null with a default value for id

-- Create the table id_not_null if it doies not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
