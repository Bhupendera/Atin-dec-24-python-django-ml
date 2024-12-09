# Hands-On: Python Database Connectivity with MS SQL

## Prerequisites
1. Install Python (3.x).
2. Install `pyodbc` library:
   ```bash
   pip install pyodbc
   ```
3. Install the Microsoft ODBC Driver for SQL Server.

---
## Driver:
```
https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
```

## Task 1: Connecting Python to MS SQL
1. Open a Python IDE or text editor.
2. Write a script to connect to the database:
```python
import pyodbc

drivers = pyodbc.drivers()
print("Available ODBC Drivers:")
for driver in drivers:
    print(driver)

pyodbc.pooling = False

# Replace 'ODBC Driver 18 for SQL Server' with the driver version installed on your machine
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=vmsqlsvr.francecentral.cloudapp.azure.com;'
    'DATABASE=TrainingDB;'
    'UID=SuperUser;'
    'PWD=********;'
    'Encrypt=yes;'
    'TrustServerCertificate=yes;'
)

print("Connection Successful!")
conn.close()
```

3. Run the script and verify the connection.

---

## Task 2: Performing CRUD Operations
1. **Insert Data**:
   ```python
   cursor = conn.cursor()
   cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", 'Alice', 28, 'HR')
   conn.commit()
   print("Record Inserted")
   ```
2. **Retrieve Data**:
   ```python
   cursor.execute("SELECT * FROM employees")
   for row in cursor.fetchall():
       print(row)
   ```
3. **Update Data**:
   ```python
   cursor.execute("UPDATE employees SET department = ? WHERE name = ?", 'Marketing', 'Alice')
   conn.commit()
   print("Record Updated")
   ```
4. **Delete Data**:
   ```python
   cursor.execute("DELETE FROM employees WHERE name = ?", 'Alice')
   conn.commit()
   print("Record Deleted")
   ```

---

## Task 3: Error Handling
1. Modify the script to include error handling:
   ```python
   try:
       conn = pyodbc.connect(
           'DRIVER={ODBC Driver 18 for SQL Server};'
           'SERVER=localhost;'
           'DATABASE=TrainingDB;'
           'UID=your_username;'
           'PWD=your_password'
       )
       cursor = conn.cursor()
       cursor.execute("SELECT * FROM employees")
       for row in cursor.fetchall():
           print(row)
   except pyodbc.Error as e:
       print(f"Error: {e}")
   finally:
       conn.close()
   ```

---

## Additional Exercises
1. Write a Python script to fetch employees from a specific department.
2. Create a function to handle database operations like `insert`, `update`, and `delete` dynamically.
3. Add logging to your Python script to track all database queries.


---

