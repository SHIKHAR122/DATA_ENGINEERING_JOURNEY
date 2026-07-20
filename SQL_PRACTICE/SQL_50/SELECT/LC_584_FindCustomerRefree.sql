--LEETCODE PROBLEM NUMBER 584 - FIND CUSTOMER REFREE
--Find the names of the customer that are either:
-- 1 )referred by any customer with id != 2.
-- 2)not referred by any customer.
-- Write your PostgreSQL query statement below

SELECT "name" 
FROM Customer
WHERE "referee_id" <>2  OR "referee_id" IS NULL;



