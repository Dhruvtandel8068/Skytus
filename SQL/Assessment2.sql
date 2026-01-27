create database Tandel;
use StudentDB;

create table Tandel(
  student_id INT,
  name VARCHAR(50),
  department VARCHAR(30),
  year INT,
  marks INT);


INSERT INTO Tandel VALUES
(1,'Dhruv','IT','6','95'),
(2,'Vansh','CSE','5','90'),
(3,'Taksh','BCA','4','60'),
(4,'Piyush','MCA','3','80'),
(5,'Akshay','BSC','2','75'),
(6,'ritik','M.Tech','2','55');

SELECT * FROM Tandel;

--Count total number of students
SELECT COUNT(*) AS total_students 
FROM Tandel;

--Find average marks of students 
SELECT AVG(marks) AS average_marks
FROM Tandel;

--Find highest and lowest marks
SELECT MAX(marks) AS highest_marks, MIN(marks) AS lowest_marks
FROM Tandel;

--Find department-wise average marks 
SELECT department, AVG(marks) AS avg_marks
FROM Tandel
GROUP BY department;

--Display departments where average marks > 70
SELECT department, AVG(marks) AS avg_marks
FROM Tandel
GROUP BY department
HAVING AVG(marks) > 70;
