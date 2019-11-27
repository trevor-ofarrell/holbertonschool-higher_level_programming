-- query to find cities in california
SELECT id, name
FROM DATABASE hbtn_0d_usa
WHERE hbtn_0d_usa.states.state_id =
     (SELECT id
     FROM hbtn_0d_usa.states
     WHERE name = "California")
ORDER BY hbtn_od_usa.cities.id ASC;
