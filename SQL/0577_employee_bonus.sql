SELECT E.name, B.bonus
FROM Employee E
LEFT JOIN Bonus B ON E.empId = B.empId
WHERE COALESCE(B.bonus, 0) < 1000
-- WHERE B.bonus < 1000 OR B.bonus IS NULL