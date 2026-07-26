CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
	movie_id SERIAL PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	release_date DATE,
	genres VARCHAR,
	vote_average NUMERIC(3, 1),
	vote_count INT,
	runtime INT,
	budget INT,
	revenue INT
)"""

DROP_TABLE = """DROP TABLE IF EXISTS movies"""


TO_BIGINT = """ALTER TABLE movies
ALTER COLUMN budget TYPE bigint,
ALTER COLUMN revenue TYPE bigint"""


TO_CSV = """COPY movies TO 'path' WITH CSV HEADER;"""


CREATE_GENRES_TABLE = """CREATE TABLE IF NOT EXISTS genres (
 genre_id serial PRIMARY KEY,
 genre_name varchar(255) UNIQUE NOT null
);"""


INSERT_INTO_GENRES = """INSERT INTO genres (genre_name)
SELECT DISTINCT trim(UNNEST(STRING_to_array(genres, ',')))
FROM MOVIES m
WHERE genres IS NOT null"""


CREATE_GENRE_MOVIE_TABLE = """CREATE TABLE IF NOT EXISTS movie_genre (
	movie_id int REFERENCES movies(movie_id),
	genre_id int REFERENCES genres(genre_id),
	PRIMARY KEY (movie_id, genre_id)
);"""


CROSS_TABLE = """INSERT INTO movie_genre (movie_id, genre_id)
SELECT 
	m.movie_id,
	g.genre_id
FROM movies m
CROSS JOIN LATERAL UNNEST(string_to_array(m.genres, ',')) AS t(genre_name)
JOIN genres g ON g.genre_name = trim(t.genre_name);"""


DELETE_COLUMN = """ALTER TABLE MOVIES 
DROP COLUMN genres; """