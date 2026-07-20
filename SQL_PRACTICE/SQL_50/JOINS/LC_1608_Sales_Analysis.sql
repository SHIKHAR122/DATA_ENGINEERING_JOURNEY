--  LEETCODE PROBLEM NUMBER 1608 - SALES ANALYSIS 

-- Table: Product

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | product_id   | int     |
-- | product_name | varchar |
-- +--------------+---------+
-- product_id is the primary key (column with unique values) of this table.
-- Each row of this table indicates the product name of each product.
 

-- Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

-- Return the resulting table in any order.

-- The result format is in the following example.





SELECT 
     product_name , 
     year , 
     price 
FROM Sales 
JOIN Product 
ON Product.product_id = Sales.product_id
