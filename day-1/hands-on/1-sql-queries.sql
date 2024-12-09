CREATE DATABASE TrainingDB;

USE TrainingDB;

CREATE TABLE employees (
   id INT PRIMARY KEY IDENTITY(1,1),
   name NVARCHAR(100),
   age INT,
   department NVARCHAR(50)
);

INSERT INTO employees (name, age, department)
VALUES ('Alice', 28, 'HR'),
	  ('Bob', 34, 'IT'),
	  ('Charlie', 25, 'Finance');

SELECT * FROM employees;

UPDATE employees SET department = 'Marketing' WHERE name = 'Alice';

DELETE FROM employees WHERE name = 'Bob';

CREATE TABLE departments (
   department_id INT PRIMARY KEY IDENTITY(1,1),
   department_name NVARCHAR(100)
);

INSERT INTO departments (department_name)
VALUES ('HR'), ('IT'), ('Finance');

SELECT employees.name, departments.department_name
FROM employees
JOIN departments ON employees.department = departments.department_name;
