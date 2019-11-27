-- script to list all cites in db
SELECT cities.id, cities.name, states.name
FROM cities, states
ORDER BY id ASC;
