-- lists all cities found in california
-- uses database hbtn_0d_usa
SELECT id, state_id, name FROM cities WHERE state_id IN
    (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California') ORDER BY cities.id ASC;