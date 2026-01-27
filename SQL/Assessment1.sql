create database StudentDB;
use StudentDB;

create table Student(
  student_id INT,
  name VARCHAR(50),
  department VARCHAR(30),
  year INT,
  marks INT);


INSERT INTO student VALUES
(1,'Dhruv','IT','6','95'),
(2,'Vansh','CSE','5','90'),
(3,'Taksh','BCA','4','85'),
(4,'Piyush','MCA','3','80'),
(5,'Akshay','BSC','2','75');


--Display all student records
SELECT * FROM student;

--Display only name and department
SELECT name, department FROM student;

--Display students with marks greater than 75
SELECT * FROM student
WHERE marks > 75;

--Display students from IT department
SELECT * FROM student
WHERE department = 'IT';

--Sort students by marks (descending)
SELECT * FROM student
ORDER BY marks DESC;

--Display top 3 scorers	
SELECT Top 3 * FROM student
ORDER BY marks DESC