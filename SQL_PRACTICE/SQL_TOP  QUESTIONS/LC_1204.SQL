-- LEETCODE PROBLEM NUMBER 1204 - LAST PERSON TO FIT IN THE BUS 

-- There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.

-- Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. -
-- The test cases are generated such that the first person does not exceed the weight limit.



WITH new_table as (
    SELECT 
         turn as Turn , 
         person_id as ID , 
         person_name , 
         weight as Weight ,
         SUM(weight)OVER(ORDER BY turn )as totalweight
    FROM Queue
)
SELECT person_name FROM new_table 
WHERE totalweight <= 1000 
ORDER BY turn DESC LIMIT 1 ;
