-- lists all shows not linked to comedy
-- genre cant be comedy
SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.title NOT IN
(SELECT tv_shows.title FROM tv_shows LEFT OUTER JOIN
    (tv_show_genres LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id AND tv_genres.name = 'Comedy')
    ON tv_shows.id = show_id
    WHERE tv_genres.name IS NOT NULL)
    ORDER BY tv_shows.title ASC;