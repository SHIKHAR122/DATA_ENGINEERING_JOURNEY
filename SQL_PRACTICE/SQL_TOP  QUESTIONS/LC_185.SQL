--  LEETCODE PROBLEM NUMBER 185 - DEPARTMENT TOP THREE SALARY 

-- A company's executives are interested in seeing who earns the most money in each of the company's departments. 
--A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

-- Write a solution to find the employees who are high earners in each of the departments.


WITH new_table as(
    SELECT   
         d.name as Department , 
         e.name aS Employee , 
         e.salary as Salary , 
         DENSE_RANK()OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS ranking
    FROM Employee as e
    LEFT JOIN Department as d 
    ON e.departmentId=d.id
)
SELECT Department , Employee , Salary FROM new_table WHERE ranking<=3;