--LEETCODE PROBLEM NUMBER 1729 -   FIND FOLLOWER COUNTS 

--Write a solution that will, for each user, return the number of followers.
--Return the result table ordered by user_id in ascending order.



# Write your MySQL query statement below
SELECT user_id , 
       COUNT(follower_id) as followers_count
FROM Followers
GROUP BY user_id 
ORDER BY user_id ASC ;