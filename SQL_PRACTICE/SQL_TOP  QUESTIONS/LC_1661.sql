-- LEETCODE PROBLEM NUMBER 1661 - AVERAGE TIME OF PROCESSING MACHINE 

-- There is a factory website that has several machines each running the same number of processes.
-- Write a solution to find the average time each machine takes to complete a process.

-- The time to complete a process is the 'end' timestamp minus the 'start' timestamp.
-- The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

-- The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.




SELECT 
a1.machine_id , 
ROUND(AVG(a2.timestamp-a1.timestamp),3) as processing_time 
FROM Activity as a1 
INNER JOIN Activity as a2
ON a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id AND a1.activity_type='start'AND a2.activity_type='end '
GROUP BY machine_id;