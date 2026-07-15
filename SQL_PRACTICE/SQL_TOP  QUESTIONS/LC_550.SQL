-- LEETCODE PROBLEM NUMBER 550 - GAMEPLAY ANALYSIS IV

-- Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. 
--In other words, you need to determine the number of players who logged in on the day immediately following their initial login, 
--and divide it by the number of total players.



WITH first_login as (
    SELECT 
          player_id , 
          MIN(event_date) as first_date
    FROM Activity 
    GROUP BY player_id 
)

SELECT 
     ROUND(COUNT(*) /(SELECT COUNT(*) FROM first_login),2) AS fraction
FROM first_login as f
JOIN Activity as a 
ON f.player_id = a.player_id 
WHERE a.event_date = DATE_ADD(f.first_date , INTERVAL 1 DAY) ; 