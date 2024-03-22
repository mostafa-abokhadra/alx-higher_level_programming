-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name FROM cities WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California');
