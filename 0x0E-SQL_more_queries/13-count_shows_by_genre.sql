-- lists genres and number of shows linked to INTO 
-- must have shows linked
SELECT tv_genres.name AS genre, COUNT(case when tv_show_genres.show_id and tv_show_genres.genre_id is not null and tv_show_genres.genre_id = tv_genres.id then 1 else 0 end) AS number_of_shows
    FROM tv_genres LEFT OUTER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    GROUP BY tv_genres.name
    ORDER BY 2 DESC;