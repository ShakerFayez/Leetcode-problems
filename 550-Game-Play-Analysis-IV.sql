-- Write your PostgreSQL query statement below
WITH temp as (SELECT MIN(event_date) + INTERVAL '1 DAY' min_day ,player_id FROM Activity GROUP BY player_id)

SELECT ROUND(COUNT(*)::NUMERIC/(SELECT COUNT( DISTINCT player_id) FROM Activity),2) AS fraction FROM Activity 
WHERE (player_id, event_date) IN (SELECT player_id, min_day FROM temp)