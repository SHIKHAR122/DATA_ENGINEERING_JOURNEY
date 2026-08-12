-- LEETCODE PROBLEM NUMBER 1341 MOVIE RATING
-- Table: Movies

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | movie_id      | int     |
-- | title         | varchar |
-- +---------------+---------+
-- movie_id is the primary key (column with unique values) for this table.
-- title is the name of the movie.
-- Each movie has a unique title.
-- Table: Users

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | user_id       | int     |
-- | name          | varchar |
-- +---------------+---------+
-- user_id is the primary key (column with unique values) for this table.
-- The column 'name' has unique values.
-- Table: MovieRating

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | movie_id      | int     |
-- | user_id       | int     |
-- | rating        | int     |
-- | created_at    | date    |
-- +---------------+---------+
-- (movie_id, user_id) is the primary key (column with unique values) for this table.
-- This table contains the rating of a movie by a user in their review.
-- created_at is the user's review date. 
 

-- Write a solution to:

-- Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
-- Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Movies table:
-- +-------------+--------------+
-- | movie_id    |  title       |
-- +-------------+--------------+
-- | 1           | Avengers     |
-- | 2           | Frozen 2     |
-- | 3           | Joker        |
-- +-------------+--------------+
-- Users table:
-- +-------------+--------------+
-- | user_id     |  name        |
-- +-------------+--------------+
-- | 1           | Daniel       |
-- | 2           | Monica       |
-- | 3           | Maria        |
-- | 4           | James        |
-- +-------------+--------------+
-- MovieRating table:
-- +-------------+--------------+--------------+-------------+
-- | movie_id    | user_id      | rating       | created_at  |
-- +-------------+--------------+--------------+-------------+
-- | 1           | 1            | 3            | 2020-01-12  |
-- | 1           | 2            | 4            | 2020-02-11  |
-- | 1           | 3            | 2            | 2020-02-12  |
-- | 1           | 4            | 1            | 2020-01-01  |
-- | 2           | 1            | 5            | 2020-02-17  | 
-- | 2           | 2            | 2            | 2020-02-01  | 
-- | 2           | 3            | 2            | 2020-03-01  |
-- | 3           | 1            | 3            | 2020-02-22  | 
-- | 3           | 2            | 4            | 2020-02-25  | 
-- +-------------+--------------+--------------+-------------+
-- Output: 
-- +--------------+
-- | results      |
-- +--------------+
-- | Daniel       |
-- | Frozen 2     |
-- +--------------+
-- Explanation: 
-- Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
-- Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.


-- APPROACH NUMBER 1 USING CTEs
WITH new_table AS (
    SELECT 
        m.movie_id,
        m.title,
        u.user_id,
        u.name,
        mr.rating,
        mr.created_at
    FROM Movies AS m
    JOIN MovieRating AS mr
        ON m.movie_id = mr.movie_id
    JOIN Users AS u
        ON u.user_id = mr.user_id
),

user_result AS (
    SELECT
        user_id,
        name,
        COUNT(*) OVER(PARTITION BY user_id) AS rating_count
    FROM new_table
),

movie_result AS (
    SELECT
        movie_id,
        title,
        AVG(rating) OVER(PARTITION BY movie_id) AS avg_rating
    FROM new_table
    WHERE created_at >= '2020-02-01'
      AND created_at < '2020-03-01'
)

SELECT results
FROM (
    SELECT name AS results
    FROM user_result
    ORDER BY rating_count DESC, name ASC
    LIMIT 1
) AS first_result

UNION ALL

SELECT results
FROM (
    SELECT title AS results
    FROM movie_result
    ORDER BY avg_rating DESC, title ASC
    LIMIT 1
) AS second_result;




-- APPROACH NUMBER 2 USING SUBQUERIES 

