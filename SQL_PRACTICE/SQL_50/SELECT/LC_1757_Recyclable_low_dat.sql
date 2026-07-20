-- LEETCODE PROBLEM NUMBER 1757 - RECYCLABLE AND LOW FAT PRODUCTS
--Write a solution to find the ids of products that are both low fat and recyclable.
-- Write your PostgreSQL query statement below
SELECT product_id 
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'; 