-- Write your PostgreSQL query statement below
SELECT product_name, year, price
FROM sales
INNER JOIN product
USING(product_id);