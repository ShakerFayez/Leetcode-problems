-- Write your PostgreSQL query statement below
with cte as (
    select product_id, max(change_date) as max_change_date
    from Products
    where change_date <= '2019-08-16'
    group by product_id
), product_id_cte as (
    select distinct(product_id)
    from Products
)

select p_cte.product_id, coalesce(p.new_price, 10) as price
from product_id_cte p_cte 
    left join cte on p_cte.product_id = cte.product_id
    left join Products p on p_cte.product_id = p.product_id and cte.max_change_date = p.change_date