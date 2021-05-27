-- lists all shows
-- lists all genres for each show listed
SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT OUTER JOIN
    (tv_show_genres LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
    ON tv_shows.id = show_id
    ORDER BY 1, 2 ASC;