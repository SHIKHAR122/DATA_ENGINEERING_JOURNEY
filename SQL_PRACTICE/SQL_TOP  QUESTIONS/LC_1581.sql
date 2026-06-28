-- LEETCODE PROBLEM NUMBER 1581 - CUSTOMER WHO VISITED BUT DID NOT MAKE ANY TRANSACTION 


-- Write a solution to find the IDs of the users who visited without making any 
--transactions and the number of times they made these types of visits.



SELECT v.customer_id , COUNT(v.visit_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t 
ON v.visit_id = t.visit_id 
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;