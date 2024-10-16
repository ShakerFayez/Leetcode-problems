-- Write your PostgreSQL query statement below
SELECT COALESCE(unique_id, NULL) AS unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI
USING(id);