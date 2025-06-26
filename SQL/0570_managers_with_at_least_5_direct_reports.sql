-- 570 Managers With at Least 5 Direct Reports
SELECT name
FROM Employee 
WHERE id IN
(SELECT managerId FROM Employee GROUP BY managerId
HAVING (COUNT(DISTINCT id)) >= 5)