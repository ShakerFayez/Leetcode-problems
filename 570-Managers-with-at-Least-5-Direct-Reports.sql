-- Write your PostgreSQL query statement below
SELECT name
FROM employee AS t1
JOIN (
SELECT managerId
FROM employee
GROUP BY managerId
HAVING  COUNT(*) >= 5) AS t2
ON t1.id = t2.managerId