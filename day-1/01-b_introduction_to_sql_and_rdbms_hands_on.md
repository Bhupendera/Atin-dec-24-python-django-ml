# Hands-On: SQL and Relational Databases

## Prerequisites
1. Install **MS SQL Server** and **SQL Server Management Studio (SSMS)**.
2. Set up a sample database named `TrainingDB`.

---

## Task 1: Creating a Database and Tables
1. Open SSMS and connect to your SQL Server instance.
2. Run the following query to create a database:
   ```sql
   CREATE DATABASE TrainingDB;
   ```
3. Use the database:
   ```sql
   USE TrainingDB;
   ```
4. Create a table:
   ```sql
   CREATE TABLE employees (
       id INT PRIMARY KEY IDENTITY(1,1),
       name NVARCHAR(100),
       age INT,
       department NVARCHAR(50)
   );
   ```

---

## Task 2: Performing CRUD Operations
1. **Insert Data**:
   ```sql
   INSERT INTO employees (name, age, department)
   VALUES ('Alice', 28, 'HR'),
          ('Bob', 34, 'IT'),
          ('Charlie', 25, 'Finance');
   ```
2. **Retrieve Data**:
   ```sql
   SELECT * FROM employees;
   ```
3. **Update Data**:
   ```sql
   UPDATE employees SET department = 'Marketing' WHERE name = 'Alice';
   ```
4. **Delete Data**:
   ```sql
   DELETE FROM employees WHERE name = 'Bob';
   ```

---

## Task 3: Using Joins
1. Create a second table:
   ```sql
   CREATE TABLE departments (
       department_id INT PRIMARY KEY IDENTITY(1,1),
       department_name NVARCHAR(100)
   );
   ```
2. Insert data into `departments`:
   ```sql
   INSERT INTO departments (department_name)
   VALUES ('HR'), ('IT'), ('Finance');
   ```
3. Retrieve data using a join:
   ```sql
   SELECT employees.name, departments.department_name
   FROM employees
   JOIN departments ON employees.department = departments.department_name;
   ```

---

## Additional Exercises
1. Add new columns to the `employees` table and populate them.
2. Use aggregate functions like `COUNT`, `AVG`, and `SUM` on the data.
