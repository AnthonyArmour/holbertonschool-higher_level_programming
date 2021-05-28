-- lists sum of show ratiungs
-- tv_shows.title rating sum
SELECT DISTINCT tv_shows.title, SUM(case when tv_shows.id = tv_show_ratings.show_id then tv_show_ratings.rate else 0 end) AS rating
FROM tv_shows, tv_show_ratings
GROUP BY tv_shows.title
ORDER BY 2 DESC;