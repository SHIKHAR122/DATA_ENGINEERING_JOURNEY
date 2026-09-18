-- Write an SQL query to find the best-selling product in each product category. If there are two or more products with the same sales quantity, go by whichever product which has the higher review rating.

-- Return the category name and product name in alphabetical order of the category.

-- products Table:
-- Column Name	Type
-- product_id	integer
-- product_name	varchar
-- category_name	varchar
-- products Example Input:
-- product_id	product_name	category_name
-- 3690	Game of Thrones	Books
-- 5520	Refrigerator	Home Appliances
-- 5952	Dishwasher	Home Appliances
-- 3561	IKGAI	Books
-- product_sales Table:
-- Column Name	Type
-- product_id	integer
-- sales_quantity	integer
-- rating	decimal (1.0 - 5.0)
-- product_sales Example Input:
-- product_id	sales_quantity	rating
-- 3690	300	4.9
-- 5520	70	3.8
-- 5952	70	4.0
-- 3561	290	4.5
-- Example Output:
-- category_name	product_name
-- Books	Game of Thrones
-- Home Appliances	Dishwasher





WITH new_table AS 
(
    SELECT 
          p.product_id , 
          p.product_name , 
          p.category_name , 
          ps.rating ,
          ROW_NUMBER()OVER(PARTITION BY p.category_name ORDER BY ps.rating DESC) as rnk
    FROM products as p 
    JOIN product_sales as ps  ON p.product_id = ps.product_id
)

SELECT 
      category_name ,
      product_name 
FROM new_table 
WHERE rnk=1;