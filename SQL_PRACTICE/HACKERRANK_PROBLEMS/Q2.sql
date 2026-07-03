--  QUESTIONS RELATED TO BASIC AGGREGATES IN HACKERRANK SQL SECTION


-- QUESTION NUMBER 1
--Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. 
--She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

-- Write a query calculating the amount of error (i.e.:  average monthly salaries), and round it up to the next integer.



SELECT CEIL(AVG(salary) - AVG(REPLACE(salary, '0', '')))
FROM Employees;






-- QUESTION NUMBER 2
-- Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.770 . Round your answer to 4 decimal places.

SELECT ROUND(LONG_W , 4) FROM STATION WHERE LAT_N = ( SELECT MIN(LAT_N) FROM STATION 
WHERE LAT_N>38.7780
)
