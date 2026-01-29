-- Department Top Three Salaries
-- https://leetcode.com/problems/department-top-three-salaries/description/
-- Approach through Window Function

WITH sbquery AS (
    SELECT name, salary, departmentId,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS max_salary
    FROM Employee
)

SELECT d.name Department, s.name Employee, s.salary Salary
FROM sbquery s
JOIN Department d
ON s.departmentId = d.id
WHERE s.max_salary IN (1,2,3)


