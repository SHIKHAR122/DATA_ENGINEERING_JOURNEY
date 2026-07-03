-- LEETCODE PROBLEM NUMBER 1873 - CALCULATE SPECIAL BONUS 
--Write a solution to calculate the bonus of each employee. 
--The bonus of an employee is 100% of their salary if the ID of the employee is an odd number 
--and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
-- Write your PostgreSQL query statement below
SELECT
employee_id,
CASE
WHEN employee_id % 2 = 1
AND name NOT LIKE 'M%'
THEN salary
ELSE 0
END AS bonus
FROM Employees
ORDER BY employee_id;