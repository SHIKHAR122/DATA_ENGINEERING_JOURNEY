--LEETCODE PROBLEM NUMBER 1693 - DAILY NEEDS AND PARTNERS

--For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
--Return the result table in any order.


# Write your MySQL query statement below
SELECT  date_id , make_name,
COUNT(DISTINCT lead_id) as unique_leads ,
COUNT(DISTINCT partner_id) as unique_partners
FROM DailySales 
GROUP BY date_id , make_name;

