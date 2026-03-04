-- Script that lists all cities of California from the database hbtn_0d_usa
-- Uses a subquery to find the state id for California and filters cities by that id

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
