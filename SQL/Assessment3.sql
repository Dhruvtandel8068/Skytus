CREATE DATABASE company_db;
USE company_db;

create table employees(
  emp_id INT,
  emp_name VARCHAR(50),
  dept_id INT,
  salary INT
  )

create table departments(
   dept_id INT,
   dept_name VARCHAR(50)
   )

insert into employees values
(101,'Dhruv',1, 50000),
(102,'yash',2,80000),
(103,'Krish',4,75000),
(104,'Aryan',3,48000),
(105,'Ritik',3,52000),
(106,'Piyush',NULL,40000);

insert into departments values
(1,'HR'),
(2,'IT'),
(3,'Finance'),
(4,'Marketing');


--Display employee name with department name 
SELECT e.emp_name, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;

--Display employees earning more than 50,000 
SELECT emp_name, salary
FROM employees
WHERE salary > 50000;

--Display department-wise total salary 
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

--Display departments with more than 2 employees 
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;

--Display employees without a department
SELECT e.emp_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
