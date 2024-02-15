-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT title, genre_id FROM tv_show_genres
RIGHT JOIN tv_shows ON id = show_id
ORDER BY title, genre_id;
