-- LEETCODE PROBLEM NUMBER 570

-- MANAGERS WITH ATLEAST 5 DIRECT REPORTS 



-- Write a solution to find managers with at least five direct reports.

-- Return the result table in any order.




SELECT 
     e1.name 
FROM Employee as e1
JOIN Employee as e2
ON e1.id = e2.managerId 
GROUP BY e1.id , e2.managerId 
HAVING COUNT(*)>=5;