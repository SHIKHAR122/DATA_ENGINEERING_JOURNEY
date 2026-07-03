--  LEETCODE PROBLEM NUMBER 177 - Nth HIGHEST SALARY 
-- Write a solution to find the nth highest distinct salary from the Employee table.
-- If there are less than n distinct salaries, return null.


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT N,1
    );
END