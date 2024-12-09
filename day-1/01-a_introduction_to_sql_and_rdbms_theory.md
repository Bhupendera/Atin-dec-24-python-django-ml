# Introduction to SQL and Relational Databases

## Overview
Structured Query Language (SQL) is the standard language for managing and interacting with relational databases. Relational Database Management Systems (RDBMS) are software systems that manage data using tables, keys, and relationships.

---

## Subtopic 1: SQL Basics

### Key Concepts
1. **SELECT Statement**: Retrieve data from a table.
   - Syntax:
     ```sql
     SELECT column1, column2 FROM table_name WHERE condition;
     ```
   - Example:
     ```sql
     SELECT name, age FROM employees WHERE department = 'HR';
     ```

2. **INSERT Statement**: Add new records to a table.
   - Syntax:
     ```sql
     INSERT INTO table_name (column1, column2) VALUES (value1, value2);
     ```
   - Example:
     ```sql
     INSERT INTO employees (name, age, department) VALUES ('John Doe', 30, 'Finance');
     ```

3. **UPDATE Statement**: Modify existing records.
   - Syntax:
     ```sql
     UPDATE table_name SET column1 = value1 WHERE condition;
     ```
   - Example:
     ```sql
     UPDATE employees SET age = 31 WHERE name = 'John Doe';
     ```

4. **DELETE Statement**: Remove records from a table.
   - Syntax:
     ```sql
     DELETE FROM table_name WHERE condition;
     ```
   - Example:
     ```sql
     DELETE FROM employees WHERE department = 'Finance';
     ```

---

## Subtopic 2: Overview of RDBMS

### Key Concepts
1. **Definition**: RDBMS stores data in structured formats using tables.
2. **Primary Key**: A unique identifier for each record.
3. **Foreign Key**: A field in a table that links to a primary key in another table.

### Examples
- Table: `employees`
  - Columns: `id`, `name`, `age`, `department`
- Relationships:
  - `id` is the primary key.
  - `department_id` in another table could act as a foreign key.

---

## Hands-On Activities
Refer to the file: `01_introduction_to_sql_and_rdbms_hands_on.md`
