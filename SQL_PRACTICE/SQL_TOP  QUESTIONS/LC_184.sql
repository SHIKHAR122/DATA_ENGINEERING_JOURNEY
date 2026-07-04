-- LEETCODE PROBLEM NUMBER 184 - DEPARTMENT HIGHEST SALARY 


-- Write a solution to find employees who have the highest salary in each of the departments.



WITH new_table as (
    SELECT
         d.name as Department , 
         e.name as Employee , 
         e.salary as Salary , 
         DENSE_RANK()OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS ranking
    FROM Employee as e 
    LEFT JOIN Department as d 
    ON e.departmentId = d.id
)
SELECT Department, Employee , Salary 
FROM new_table WHERE ranking=1;



