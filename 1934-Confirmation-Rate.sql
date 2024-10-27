-- Write your PostgreSQL query statement below
SELECT user_id, ROUND(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END)::NUMERIC/COUNT(*), 2) AS confirmation_rate
FROM signups
LEFT JOIN confirmations
USING(user_id)
GROUP BY user_id
ORDER BY confirmation_rate;