-- displays avg temp by city ordered by temp DESC 
SELECT city, AVG(`value`) AS avg_temp FROM temperatures GROUP BY city ORDER BY AVG(`value`) DESC;