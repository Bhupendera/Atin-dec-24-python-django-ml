# Connecting a Django project to Microsoft SQL Server

---

### **Step 1: Install Required Packages**
Django requires a database driver to communicate with SQL Server. Use the `django-mssql-backend` or `mssql-django` package.

#### Install the Database Backend:
1. **Install the `mssql-django` package**:
   ```bash
   pip install mssql-django
   ```
   Alternatively, if you're using `django-mssql-backend`:
   ```bash
   pip install django-mssql-backend
   ```

2. **Install the Microsoft ODBC Driver**:
   - Download and install the [Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

---

### **Step 2: Update Django Settings**
In your Django project, update the `DATABASES` setting in `settings.py` to configure SQL Server as the database.

#### Example Configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'YourDatabaseName',  # Replace with your database name
        'USER': 'YourUsername',     # Replace with your username
        'PASSWORD': 'YourPassword', # Replace with your password
        'HOST': 'YourServerName',   # Replace with your server name or IP
        'PORT': '1433',             # Default SQL Server port
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Ensure this matches your installed ODBC driver
        },
    }
}
```

---

### **Step 3: Test the Connection**
1. Run Django migrations to verify the connection:
   ```bash
   python manage.py migrate
   ```

2. Check for errors in the console. If everything is set up correctly, migrations should run successfully.

---

### **Step 4: Troubleshooting**
#### Common Issues and Solutions:
1. **ODBC Driver Not Found**:
   - Ensure the correct ODBC driver is installed.
   - Verify the driver name matches the installed version (`ODBC Driver 17 for SQL Server` or later).

2. **Authentication Issues**:
   - Confirm the username and password are correct.
   - For Active Directory authentication, use the following options:
     ```python
     'OPTIONS': {
         'driver': 'ODBC Driver 17 for SQL Server',
         'authentication': 'ActiveDirectoryPassword',
     }
     ```

3. **Connection Timeout**:
   - Verify the server name or IP address is correct.
   - Ensure port `1433` is open and accessible.

4. **Dependencies Missing**:
   - On Linux, ensure `unixODBC` and related packages are installed:
     ```bash
     sudo apt-get install unixodbc-dev
     ```

---

### **Step 5: Verify Data Retrieval**
To test if the connection works, create a model and query the database.

#### Example Model:
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

#### Querying the Database:
```python
from myapp.models import Product

# Fetch all products
products = Product.objects.all()
print(products)
```

---

### **Summary**
1. Install the required packages (`mssql-django` and ODBC Driver for SQL Server).
2. Configure the `DATABASES` setting in `settings.py`.
3. Run migrations to ensure the connection is successful.
4. Troubleshoot common issues like authentication or driver problems.
