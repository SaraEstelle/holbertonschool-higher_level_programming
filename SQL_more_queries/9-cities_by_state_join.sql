-- Script that lists all cities with their state name from the database hbtn_0d_usa
-- Select city id, city name and corresponding state name, ordred by city id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
