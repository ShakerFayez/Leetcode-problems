-- Write your PostgreSQL query statement below
SELECT query_name, ROUND(AVG(rating/position::NUMERIC), 2) AS quality
, ROUND(SUM((rating < 3)::INTEGER) * 100. / COUNT(*), 2) AS poor_query_percentage
FROM queries
GROUP BY query_name
HAVING query_name IS NOT NULL;