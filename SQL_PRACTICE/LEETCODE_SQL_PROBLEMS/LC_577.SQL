-- LEETCODE PROBLEM NUMBER 577 EMPLOYEE BONUS 
-- Write a solution to report the name and bonus amount of each employee who satisfies either of the following:

-- The employee has a bonus less than 1000.
-- The employee did not get any bonus.
-- Return the result table in any order.



SELECT 
     e.name , b.bonus
FROM Employee as e 
LEFT JOIN Bonus as b 
ON e.empId = b.empId
WHERE b.bonus is null or b.bonus<1000;