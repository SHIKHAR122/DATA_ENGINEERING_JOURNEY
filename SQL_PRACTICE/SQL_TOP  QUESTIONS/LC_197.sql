-- LEETCODE  PROBLEM NUMBER 197 - RISING TEMPERATURE 

-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.



SELECT w1.id FROM Weather as w1 
INNER JOIN Weather as w2 
ON DATEDIFF(w1.recordDate , w2.recordDate) =1 
WHERE w1.temperature > w2.temperature ;