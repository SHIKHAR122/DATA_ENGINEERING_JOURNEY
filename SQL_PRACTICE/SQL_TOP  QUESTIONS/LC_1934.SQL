-- LEETCODE PROBLEM NUMBER 1934 - CONFIRMATION RATE 

-- The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. 
--The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.
-- Write a solution to find the confirmation rate of each user.


# Write your MySQL query statement below
SELECT s.user_id , 
       ROUND(IFNULL(AVG(action='confirmed'),0),2) as confirmation_rate 
FROM Signups as s 
LEFT JOIN Confirmations as c 
ON s.user_id = c.user_id 
GROUP BY user_id ;