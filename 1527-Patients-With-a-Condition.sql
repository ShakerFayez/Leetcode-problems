-- Write your PostgreSQL query statement below
SELECT *
FROM patients
WHERE conditions ~ '(^| )DIAB1'; -- '(^| )DIAB1' is Raw String like Pandas. 