--  QUESTIONS FROM ADVNACED SELECT IN HACKERRANK SQL SECTION 



--  Q1 Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. 
--Output one of the following statements for each record in the table:

-- Equilateral: It's a triangle with 3 sides of equal length.
-- Isosceles: It's a triangle with 2 sides of equal length.
-- Scalene: It's a triangle with 3 sides of differing lengths.
-- Not A Triangle: The given values of A, B, and C don't form a triangle.



SELECT CASE WHEN (A + B <= C OR A + C <= B OR B + C <= A) THEN 'Not A Triangle'
    WHEN (A = B AND B = C)
    THEN 'Equilateral'
    WHEN (A = B OR B = C OR A = C)
    THEN 'Isosceles'
    ELSE
    'Scalene'
END
FROM TRIANGLES;




-- -Q2 Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical
 --(i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
-- Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order,
-- and output them in the following format:



SELECT
    CONCAT(name, '(', LEFT(occupation, 1), ')') 
FROM Occupations
ORDER BY name ASC;
SELECT CONCAT('There are a total of',' ', COUNT(Name),' ', LOWER(Occupation), 's.') FROM OCCUPATIONS 
GROUP BY Occupation
 ORDER BY COUNT(Name)ASC, LOWER(Occupation) ASC;

