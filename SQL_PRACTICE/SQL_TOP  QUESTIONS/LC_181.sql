-- LEETCODE PROBLEM NUMBER 181 - EMPLOYEE EARNING MORE THAN THEIR MANAGERS 

-- Write a solution to find the employees who earn more than their managers.

-- Return the result table in any order.




SELECT e2.name AS Employee 
FROM Employee as e1 
INNER JOIN Employee as e2 
ON e1.id = e2.managerId
WHERE e1.salary < e2.salary

