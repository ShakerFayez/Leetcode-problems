-- Write your PostgreSQL query statement below
WITH rank_cte AS (
    SELECT Department.name AS Department, Employee.name AS Employee, salary, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS rank
    FROM Employee
    JOIN Department
    ON Employee.departmentId = Department.id
)

SELECT Department, Employee, salary
FROM rank_cte 
WHERE rank <= 3;