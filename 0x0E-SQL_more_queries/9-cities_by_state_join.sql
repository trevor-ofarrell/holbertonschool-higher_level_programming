-- script to list all cites in db
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.id = states.id
ORDER BY city.id ASC;
