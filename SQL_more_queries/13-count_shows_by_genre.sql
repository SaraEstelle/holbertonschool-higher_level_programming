-- Script that lists all genres and the number of shows linked from hbtn_0d_tvshows

SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id IS NOT NULL
GROUP BY genres.name
ORDER BY number_of_shows DESC;
