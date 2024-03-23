-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- The database name will be passed as an argument of the mysql command
SELECT name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows from tv_genres 
INNER JOIN tv_show_genres 
ON id = tv_show_genres.genre_id
group by tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
