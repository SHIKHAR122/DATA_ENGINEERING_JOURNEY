--  LEETCODE PROBLEM NUMBER 1193 - MONTHLY TRANSACTIONS 

-- Write an SQL query to find for each month and country, the number of transactions and their total amount, 
--the number of approved transactions and their total amount.


SELECT
     LEFT(trans_date, 7) AS month,
     country , 
     COUNT(id) AS trans_count ,
     SUM(state='approved') AS approved_count , 
     SUM(amount) AS trans_total_amount ,
     SUM((state='approved')*amount) AS approved_total_amount

FROM Transactions 
GROUP BY month , country ; 
