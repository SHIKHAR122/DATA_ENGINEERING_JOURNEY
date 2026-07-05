-- LEETCODE PROBLEM NUMBER 180 - CONSECUTIVE NUMBERS

-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.



SELECT DISTINCT num AS ConsecutiveNums 
FROM (
    SELECT 
         num , 
         LAG(num,1)OVER(ORDER BY id) as prev1 , 
         LAG(num,2)OVER(ORDER BY id ) as prev2
    FROM Logs
)t

WHERE prev1=num AND num=prev2;