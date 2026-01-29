-- ya daun dazhe xz che skazat, no rabotaet
-- https://leetcode.com/problems/trips-and-users/description/

WITH strng_shit AS (
SELECT t.request_at Day, COUNT(*) cnt,
    CASE WHEN t.status = 'completed' THEN CONCAT(CAST(DATE_FORMAT(t.request_at, '%Y-%m-%d') AS char), 'compl')
    ELSE CONCAT(CAST(DATE_FORMAT(t.request_at, '%Y-%m-%d') AS char), 'cancld') END AS extra_column
FROM Trips t
JOIN Users u
ON t.client_id = u.users_id
JOIN Users d
ON t.driver_id = d.users_id
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
AND d.banned <> 'Yes' AND u.banned <> 'Yes'
GROUP BY 3
)

SELECT s.Day Day, ROUND(s.rt, 2) as 'Cancellation Rate'
FROM (
SELECT Day,
    CASE WHEN cnt / SUM(cnt) OVER(PARTITION BY Day) = 1 AND extra_column LIKE '%compl' THEN 0
    WHEN cnt / SUM(cnt) OVER(PARTITION BY Day) = 1 AND extra_column LIKE '%cancld' THEN 1
    ELSE cnt / SUM(cnt) OVER(PARTITION BY Day) END as 'rt',
    extra_column
FROM strng_shit
) s
WHERE s.extra_column LIKE '%cancld'
OR s.rt = 0