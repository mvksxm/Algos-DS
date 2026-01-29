-- My approach (The most optimal) (Join the bigger date on the date that is smaller by one day)
SELECT w.id id
FROM Weather w
JOIN Weather s
ON w.recordDate = DATE_ADD(s.recordDate, INTERVAL 1 DAY)
WHERE w.temperature > s.temperature


-- CROSS JOIN Approach
SELECT w.id id
FROM Weather w
CROSS JOIN Weather s
WHERE DATEDIFF(w.recordDate, s.recordDate) = 1
AND w.temperature > s.temperature