--LEETCODE PROBLEM NUMBER 176 - SECOND HIGHEST SALARY 
-- Write a solution to find the second highest distinct salary from the Employee table. 
-- If there is no second highest salary, return null 

-- FIRST APPROACH USING THE COALESCE- 

SELECT COALESCE(
(
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
),
NULL) AS SecondHighestSalary;


