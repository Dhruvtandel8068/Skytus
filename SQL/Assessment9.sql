CREATE DATABASE TestDB;
USE TestDB;

CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    salary INT,
    hire_date DATE
);

CREATE TABLE emp_backup (
    emp_id INT,
    emp_name VARCHAR(50),
    salary INT
);
CREATE TABLE logs (
    id INT,
    value INT
);


INSERT INTO employees VALUES
(1, 'Dhruv', 60000, '2026-01-10'),
(2, 'Taksh', 80000, '2025-12-05'),
(3, 'Aryan', 70000, '2025-09-15'),
(4, 'Krish', 80000, '2025-11-20'),
(5, 'Yash', 60000, '2025-08-05'),
(6, 'Vansh', 50000, '2026-01-01');



INSERT INTO emp_backup VALUES
(1, 'Dhruv', 60000),
(2, 'Taksh', 80000),
(4, 'Krish', 80000),
(6, 'Vansh', 50000);

INSERT INTO logs VALUES
(1, 10),
(2, 10),
(3, 10),
(4, 20),
(5, 30),
(6, 30);

--Write query to find Nth highest salary 
SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk = 4;

--Remove duplicate records 
WITH cte AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY emp_name, salary, hire_date
               ORDER BY emp_id
           ) AS rn
    FROM employees
)
DELETE FROM cte
WHERE rn > 1;


--Find records common in two tables 
SELECT emp_id, emp_name, salary
FROM employees
INTERSECT
SELECT emp_id, emp_name, salary
FROM emp_backup;

--Find employees hired in last 6 months 
SELECT *
FROM employees
WHERE hire_date >= DATEADD(MONTH, -6, GETDATE());

--Find continuous duplicate values
SELECT DISTINCT value
FROM (
    SELECT value,
           LAG(value) OVER (ORDER BY id) AS prev_value
    FROM logs
) t
WHERE value = prev_value;
