-- displays comedy shows
-- must have comedy genre
SELECT tv_shows.title FROM tv_shows LEFT OUTER JOIN (tv_show_genres LEFT OUTER JOIN tv_genres ON tv_genres.name = 'Comedy')
    ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_show_genres.genre_id = tv_genres.id
    ORDER BY tv_shows.title