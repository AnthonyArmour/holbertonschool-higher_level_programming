-- lists all cities in hbtn_0d_usa DATABASE 
-- id cities.name states.name
SELECT cities.id, cities.name, states.name FROM cities LEFT OUTER JOIN states ON cities.state_id = states.id;