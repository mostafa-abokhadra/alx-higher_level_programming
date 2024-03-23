--  script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The database name will be passed as an argument of the mysql command

-- first solution
/*
SLECT tv_shows.title FROM tv_shows
inner join tv_show_genres ON tv_shows.id = tv_show_genres.show_id
where tv_show_genres.genre_id = 
(slect tv_genres.id from tv_genres where tv_genres.name = 'Comedy');
order by title;
*/

-- another method
/*
SLECT tv_shows.title FROM tv_shows
inner join tv_show_genres inner join tv_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id = tv_genres.id and tv_genres.name = 'Comedy';
order by tv_shows.title;
*/

-- another method
/*
SLECT tv_shows.title FROM tv_shows
inner join tv_show_genres ON tv_shows.id = tv_show_genres.show_id
inner join tv_genres
WHERE tv_show_genres.genre_id = tv_genres.id and tv_genres.name = 'Comedy';
order by title;
*/


-- the best solution
SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
