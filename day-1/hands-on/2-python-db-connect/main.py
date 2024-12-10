import pyodbc
import common

common.hello()

drivers = pyodbc.drivers()
print("Available ODBC Drivers:")
for driver in drivers:
    print(driver)

pyodbc.pooling = False

try:
    # Replace 'ODBC Driver 18 for SQL Server' with the driver version installed on your machine
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=vmsqlsvr.francecentral.cloudapp.azure.com;'
        'DATABASE=TrainingDB;'
        'UID=SuperUser;'
        'PWD=Azure@123456;'
        'Encrypt=yes;'
        'TrustServerCertificate=yes;'
    )

    print("Connection Successful!")

    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", 'Alice', 28, 'HR')
    conn.commit()
    print("Record Inserted")

    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("UPDATE employees SET department = ? WHERE name = ?", 'Marketing', 'Alice')
    conn.commit()
    print("Record Updated")

    cursor.execute("DELETE FROM employees WHERE name = ?", 'Alice')
    conn.commit()
    print("Record Deleted")

except pyodbc.Error as e:
   print(f"Error: {e}")
finally:
   conn.close()

