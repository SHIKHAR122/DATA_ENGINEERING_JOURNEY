--  LEETCODE PROBLEM NUMBER 196  - DUPLICATE EMAIL 

-- Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.


DELETE p1 
FROM Person as p1
JOIN Person as p2 
ON p1.email=p2.email 
AND p1.id>p2.id ; 