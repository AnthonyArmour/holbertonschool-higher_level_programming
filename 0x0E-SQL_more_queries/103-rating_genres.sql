-- lists sum of genre ratiungs
-- tv_genres.name rating sum
SELECT DISTINCT tv_genres.name, SUM(case when tv_shows.id = tv_show_ratings.show_id AND
    tv_genres.id = tv_show_genres.genre_id and tv_shows.id = tv_show_genres.show_id
    then tv_show_ratings.rate else 0 end) AS rating
FROM tv_shows, tv_show_ratings, tv_show_genres, tv_genres
GROUP BY tv_genres.name
ORDER BY 2 DESC;