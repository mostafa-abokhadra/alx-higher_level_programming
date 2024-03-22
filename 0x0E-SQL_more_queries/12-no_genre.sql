-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- The database name will be passed as an argument of the mysql command
SELECT title, genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id where tv_show_genres.show_id IS NULL;
