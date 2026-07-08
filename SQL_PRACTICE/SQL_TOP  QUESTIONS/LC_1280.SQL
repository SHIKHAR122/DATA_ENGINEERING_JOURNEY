-- LEETCODE PROBLEM NUMBER 1280 - STUDENTS AND EXAMINATIONS 


-- Write a solution to find the number of times each student attended each exam.

-- Return the result table ordered by student_id and subject_name.



WITH new_table AS (
    SELECT
        s.student_id,
        s.student_name,
        sub.subject_name
    FROM Students as s
    CROSS JOIN Subjects as sub
)
SELECT
    nt.student_id,
    nt.student_name,
    nt.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM new_table  as nt
LEFT JOIN Examinations as e
    ON nt.student_id = e.student_id
   AND nt.subject_name = e.subject_name
GROUP BY
    nt.student_id,
    nt.student_name,
    nt.subject_name
ORDER BY
    nt.student_id,
    nt.subject_name;