-- LEETCODE PROBLEM NUMBER 620 - NOT BORING MOVIES 
--Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

# Write your MySQL query statement below
SELECT * FROM Cinema WHERE id % 2 =1  AND description != 'boring' ORDER BY rating DESC;