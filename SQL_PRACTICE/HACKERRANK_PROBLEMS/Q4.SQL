-- QUESTIONS FROM HACKKERANK BASED ON BASIC JOINS 

-- QUESTION NUMBER 1 - Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.


SELECT SUM(c.POPULATION) 
FROM CITY AS c 
LEFT JOIN COUNTRY AS country
ON c.COUNTRYCODE = country.CODE
WHERE CONTINENT = 'ASIA';






-- QUESTION NUMBER 2 Given the CITY and COUNTRY tables, 
-- query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.



SELECT CY.Continent, 
FLOOR(AVG(C.Population)) 
FROM City AS C 
JOIN Country AS CY 
ON C.CountryCode = CY.Code 
GROUP BY CY.Continent;








-- QUESTION NUMBER 3 
-- Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. 
-- Ketty doesn't want the NAMES of those students who received a grade lower than 8. 
-- The report must be in descending order by grade -- i.e. higher grades are entered first.
-- If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. 
--Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. 
--If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

-- Write a query to help Eve.



SELECT 
    CASE 
        WHEN G.GRADE < 8 THEN NULL
        ELSE S.NAME
    END AS NAME,
    G.GRADE,
    S.MARKS
FROM STUDENTS S
INNER JOIN GRADES G ON S.MARKS >= G.MIN_MARK AND S.MARKS <= G.MAX_MARK
ORDER BY 
    G.GRADE DESC,
    CASE WHEN G.GRADE >= 8 THEN S.NAME END ASC,
    CASE WHEN G.GRADE < 8 THEN S.MARKS END ASC;
