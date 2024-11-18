SELECT e1.employee_id, e1.name, COUNT(e2.reports_to) reports_count, AVG(e2.age)::int average_age
FROM Employees e1
         JOIN Employees e2 on e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, e1.name
ORDER BY e1.employee_id