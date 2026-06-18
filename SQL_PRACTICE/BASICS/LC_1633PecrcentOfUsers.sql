--LEETCODE PROBLEM NUMBER 1633  PRECENTAGE OF USERS ATTENDED THE CONTEST
--Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

--Return the result table ordered by percentage in descending order. 
--In case of a tie, order it by contest_id in ascending order.


WITH total_users AS (
    SELECT COUNT(user_id)  AS counter
    FROM Users
)

SELECT contest_id ,
ROUND(COUNT(DISTINCT user_id)*100.0 /counter , 2) AS percentage
FROM Register
CROSS JOIN total_users
GROUP BY contest_id 
ORDER BY percentage DESC , contest_id;