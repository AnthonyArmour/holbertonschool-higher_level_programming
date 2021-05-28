-- lists all genres not linked to dexter
-- genre cant be linked to dexter
SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.name NOT IN
(SELECT tv_genres.name FROM tv_shows LEFT OUTER JOIN
    (tv_show_genres LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
    ON tv_shows.id = show_id and tv_shows.title = "Dexter"
    WHERE tv_genres.name IS NOT NULL)
    ORDER BY tv_genres.name ASC;