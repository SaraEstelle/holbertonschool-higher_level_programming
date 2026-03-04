-- Lists all shows and their genre_id from hbtn_0d_tvshows

SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY title ASC, genre_id ASC;