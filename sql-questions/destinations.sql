-- https://youtu.be/WhkNQ3g0U64
-- Special Pattern
-- Approach - ROW_NUMBER() window func, Self-join

SELECT s.source Source, s.destination Destination, s.distance Distance
FROM (
	SELECT f.source AS source, f.destination destination, f.distance distance,
	ROW_NUMBER() OVER() AS 'row_number'
	FROM distances f
	JOIN distances s
	ON f.source = s.destination
	AND f.destination = s.source
) as s
WHERE s.row_number % 2 <> 0