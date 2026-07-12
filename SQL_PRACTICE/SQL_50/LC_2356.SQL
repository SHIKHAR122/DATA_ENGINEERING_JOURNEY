--  LEETCODE PROBLEM NUMBER 2356 - NUMBER OF UNIQUE SUBJECTS TAUGHT BY EACH TEACHER 

-- Write a solution to calculate the number of unique subjects each teacher teaches in the university.

-- Return the result table in any order.



SELECT 
     teacher_id  ,
     COUNT(DISTINCT subject_id ) as cnt

FROM Teacher 
GROUP BY teacher_id 