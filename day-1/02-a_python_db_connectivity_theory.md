# Python Database Connectivity with MS SQL

## Overview
Python provides powerful libraries like `pyodbc` for interacting with relational databases such as MS SQL Server. This session focuses on establishing database connectivity, executing SQL queries, and performing CRUD operations from Python.

---

## Subtopic 1: Setting Up Python for Database Connectivity

### Key Concepts
1. **Required Tools and Libraries**:
   - Python: Ensure Python 3.x is installed.
   - `pyodbc`: A Python library for ODBC database connectivity.
     ```bash
     pip install pyodbc
     ```
   - Microsoft ODBC Driver for SQL Server: Allows Python to connect to MS SQL databases.

2. **Connection String**:
   - A connection string contains information required to connect to the database.
   - Components:
     - **DRIVER**: ODBC driver name.
     - **SERVER**: Database server address.
     - **DATABASE**: Target database name.
     - **UID** and **PWD**: Credentials for authentication.

3. **Sample Connection String**:
   ```python
   conn = pyodbc.connect(
       'DRIVER={ODBC Driver 17 for SQL Server};'
       'SERVER=localhost;'
       'DATABASE=TrainingDB;'
       'UID=your_username;'
       'PWD=your_password'
   )
   ```

---

## Subtopic 2: CRUD Operations Using Python

### Key Concepts
1. **Creating Data**:
   - Use the `INSERT` statement to add records.
   - Example:
     ```python
     cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", 'David', 29, 'Marketing')
     conn.commit()
     ```

2. **Reading Data**:
   - Use the `SELECT` statement to fetch data.
   - Example:
     ```python
     cursor.execute("SELECT * FROM employees")
     for row in cursor.fetchall():
         print(row)
     ```

3. **Updating Data**:
   - Use the `UPDATE` statement to modify records.
   - Example:
     ```python
     cursor.execute("UPDATE employees SET department = ? WHERE name = ?", 'Sales', 'Alice')
     conn.commit()
     ```

4. **Deleting Data**:
   - Use the `DELETE` statement to remove records.
   - Example:
     ```python
     cursor.execute("DELETE FROM employees WHERE name = ?", 'Bob')
     conn.commit()
     ```

---

## Subtopic 3: Error Handling in Database Operations

### Key Concepts
1. **Using `try-except` Blocks**:
   - Handle potential errors such as invalid queries or connection issues.
   - Example:
     ```python
     try:
         conn = pyodbc.connect(...)
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM employees")
     except pyodbc.Error as e:
         print(f"Error: {e}")
     finally:
         conn.close()
     ```

2. **Common Errors**:
   - Invalid credentials.
   - Connection timeouts.
   - Syntax errors in SQL statements.

---

## Hands-On Activities
Refer to the file: `02_python_db_connectivity_hands_on.md`

---

