-- 1731 The Number of Employees Which Report to Each Employee
SELECT mgr.employee_id, mgr.name, COUNT(emp.reports_to) AS reports_count, ROUND(AVG(emp.age)) AS average_age
FROM Employees emp
JOIN Employees mgr ON emp.reports_to = mgr.employee_id
GROUP BY mgr.employee_id, mgr.name
ORDER BY mgr.employee_id