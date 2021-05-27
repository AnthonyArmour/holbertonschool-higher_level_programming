-- lists all genres of specific SHOW 
-- show is Dexter
SELECT tv_genres.name FROM tv_genres LEFT OUTER JOIN (tv_show_genres LEFT OUTER JOIN tv_shows ON tv_shows.title = 'Dexter')
    ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_genres.name;