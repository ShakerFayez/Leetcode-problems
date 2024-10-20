-- Write your PostgreSQL query statement below
SELECT name, bonus
FROM employee
LEFT JOIN bonus
USING(empId)
WHERE bonus IS NULL 
OR bonus < 1000;