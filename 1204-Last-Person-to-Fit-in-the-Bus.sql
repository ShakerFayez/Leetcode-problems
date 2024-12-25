-- Write your PostgreSQL query statement below
WITH running_total AS (
    SELECT person_name, SUM(weight) OVER(ORDER BY turn ASC) AS total_weight
    FROM Queue
)

SELECT person_name
FROM running_total
WHERE total_weight <= 1000 
ORDER BY total_weight DESC
LIMIT 1