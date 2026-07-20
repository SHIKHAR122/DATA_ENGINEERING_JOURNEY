-- LEETCODE PROBLEM NUMBER 1378 - REPLACE EMPLOYEE ID WITH THE UNIQUE IDENTIFIER

-- Write a solution to show the unique ID of each user, 
--If a user does not have a unique ID replace just show null.



SELECT u.unique_id, e.name 
FROM Employees as e 
LEFT JOIN EmployeeUNI AS u 
ON e.id = u.id ;
