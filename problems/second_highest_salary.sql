-- https://leetcode.com/problems/second-highest-salary/

-- Solution 1
SELECT
    IFNULL(
        (
            SELECT DISTINCT Salary
            FROM Employee
            ORDER BY Salary DESC
            LIMIT 1 OFFSET 1
        ),
        NULL
    ) AS SecondHighestSalary;

-- Solution 2
SELECT
    (
        SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary;

-- Solution 3
SELECT max(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee);
