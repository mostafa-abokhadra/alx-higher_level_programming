-- script that creates the table unique_id on your MySQL server.
-- The database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
