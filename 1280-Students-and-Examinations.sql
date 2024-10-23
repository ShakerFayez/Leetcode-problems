-- Write your PostgreSQL query statement below
SELECT t1.student_id, t1.student_name, t1.subject_name, COUNT(e.subject_name) AS attended_exams
FROM (SELECT * FROM students, subjects) AS t1
LEFT JOIN examinations as e
ON t1.student_id = e.student_id
AND t1.subject_name = e.subject_name
GROUP BY t1.student_id, t1.student_name, t1.subject_name
ORDER BY t1.student_id, t1.subject_name;