-- 1204 Last Person to Fit in the Bus
SELECT person_name
FROM 
(SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
) AS Ordered_queue
WHERE cumulative_weight <= 1000
ORDER BY turn DESC
LIMIT 1