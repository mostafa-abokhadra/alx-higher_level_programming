-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The database name will be passed as an argument of the mysql command

/*SELCT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres INNER JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = tv_shows.id and tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
*/
-- above code works but this is better and more readable:
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
