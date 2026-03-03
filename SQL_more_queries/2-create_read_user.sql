-- Script that creates the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege only

-- Create the database hbtn_0d_2 if it does not already exist
CREATE DATABASE IF NOT EXISTS HBTN_0d_2;

-- Create user user_0d_2 if it does not alreadt exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply privilege changes
FLUSH PRIVILEGES;
