--  LEETCODE PROBLEM NUMBER 610 - TRIANGLE JUDGMENT 


--Report for every three line segments whether they can form a triangle.

-- Return the result table in any order.



SELECT x,y,z,
       CASE 
          WHEN x+y>z 
          AND x+z > y
          AND y+z>x
          THEN 'Yes'
          ELSE 'No'
    END AS triangle
FROM triangle ; 




-- ANOTHER APPROACH FOR THIS PROBLEM IS - 

SELECT * , 
IF (
    x+y>z AND x+z>y AND y+z>x , 'Yes' , 'No'
) as triangle 
FROM triangle ; 