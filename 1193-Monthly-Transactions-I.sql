WITH approved AS (
    SELECT 
        TO_CHAR(trans_date, 'YYYY-MM') AS month, 
        country, 
        COUNT(*) AS approved_count,
        SUM(amount) AS approved_total_amount
    FROM transactions
    WHERE state = 'approved'
    GROUP BY month, country
)

SELECT 
    TO_CHAR(t.trans_date, 'YYYY-MM') AS month, 
    t.country, 
    COUNT(*) AS trans_count,
    SUM(t.amount) AS trans_total_amount, 
    COALESCE(a.approved_count, 0) AS approved_count, 
    COALESCE(a.approved_total_amount, 0) AS approved_total_amount
FROM transactions AS t
LEFT JOIN approved AS a
    ON TO_CHAR(t.trans_date, 'YYYY-MM') = a.month 
    AND (t.country = a.country OR (t.country IS NULL AND a.country IS NULL))
GROUP BY TO_CHAR(t.trans_date, 'YYYY-MM'), t.country, a.approved_count, a.approved_total_amount;
