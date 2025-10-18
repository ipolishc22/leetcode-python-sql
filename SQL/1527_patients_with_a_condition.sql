-- 1527 Patients with a condition
SELECT *
FROM Patients
WHERE conditions LIKE "DIAB1%" OR conditions LIKE "% DIAB1%"