-- lists all shows without genre_id
-- must have null genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT OUTER JOIN tv_show_genres ON
    tv_show_genres.show_id = tv_shows.id WHERE tv_show_genres.genre_id IS NULL
    ORDER BY tv_shows.title, tv_show_genres.genre_id;