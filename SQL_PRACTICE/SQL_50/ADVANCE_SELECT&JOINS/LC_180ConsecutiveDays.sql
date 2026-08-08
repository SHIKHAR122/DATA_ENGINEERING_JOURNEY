-- -- LEETCODE PROBLEM NUMBER 180 CONSECUTIVE DAYS 

-- Table: Logs

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column starting from 1.
 

-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Logs table:
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- Output: 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- Explanation: 1 is the only number that appears consecutively for at least three times.




-- APPROACH NUMBER 1 , USING CTE 

WITH new_table as(
    SELECT 
         num , 
         LAG(num , 1) OVER(ORDER BY id ) AS c1 , 
         LAG(num , 2) OVER(ORDER BY id ) AS c2
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums FROM new_table 
WHERE num=c1 AND num=c2;


-- APPROACH NUMBER 2 , USING SUBQUERY 

SELECT DISTINCT num as ConsecutiveNums
FROM (

    SELECT  
          num, 
          LAG(num , 1 ) OVER (ORDER BY id ASC) AS con1 , 
          LAG(num , 2) OVER (ORDER BY id ASC) AS con2
    FROM Logs
)t
WHERE num = con1 AND  num = con2;