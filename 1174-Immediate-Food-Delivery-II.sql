-- Write your PostgreSQL query statement below
WITH FirstOrder AS (
SELECT
    customer_id,
    MIN(order_date) as order_date
FROM Delivery
GROUP BY customer_id
)

SELECT ROUND(AVG(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 ELSE 0 END) * 100, 2) AS immediate_percentage
FROM Delivery d
INNER JOIN FirstOrder fo on fo.customer_id = d.customer_id AND fo.order_date = d.order_date;