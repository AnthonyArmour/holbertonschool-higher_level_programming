-- displays top 3 cities temps during july and august
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY AVG(`value`) DESC LIMIT 3; 