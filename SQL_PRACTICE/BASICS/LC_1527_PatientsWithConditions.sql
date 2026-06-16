-- LEETCODE PROBLEM NUMBER 1527 PATIENTS WITH CONDITIONS 
--Write a solution to find the patient_id, patient_name, 
--and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

SELECT * 
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'
