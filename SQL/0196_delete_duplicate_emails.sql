-- 196 Delete duplicate emails 
DELETE p2
FROM Person p1
JOIN PErson p2 ON p1.email = p2.email 
AND p1.id < p2.id