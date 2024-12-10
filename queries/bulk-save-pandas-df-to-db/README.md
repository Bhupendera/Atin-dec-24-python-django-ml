# Using pandas and SQLAlchemy to Handle CSV Data and Save to Database

## **1. Introduction**
This document explains how to use **pandas** and **SQLAlchemy** to:
1. Load data from a CSV file into a pandas DataFrame.
2. Save the DataFrame to a database table in bulk.
3. Perform basic data verification in the database.

---

## **2. pandas Overview**
pandas is a Python library for data analysis and manipulation. It is widely used for handling structured data like CSV, Excel, and JSON files.

### Key Concepts:
- **DataFrame**:
  - A 2D labeled data structure, similar to a table.
- **Series**:
  - A 1D labeled array, like a single column in a table.

---

## **3. SQLAlchemy Overview**
SQLAlchemy is a powerful SQL toolkit and ORM for Python. It allows seamless integration of Python applications with relational databases.

### Key Concepts:
1. **Engine**:
   - Establishes a connection to the database.
   - Example:
     ```python
     from sqlalchemy import create_engine
     engine = create_engine('sqlite:///example.db')
     ```

2. **Declarative Base**:
   - The foundation for defining ORM models.
   - Example:
     ```python
     from sqlalchemy.ext.declarative import declarative_base
     Base = declarative_base()
     ```

3. **Session**:
   - Manages transactions and interactions with the database.
   - Example:
     ```python
     from sqlalchemy.orm import sessionmaker
     Session = sessionmaker(bind=engine)
     session = Session()
     ```

---

## **4. Reading CSV Data with pandas**
### Loading a CSV File:
The `read_csv` function loads CSV data into a DataFrame:
```python
import pandas as pd
df = pd.read_csv('users.csv')
print(df)
```

### Common Parameters:
- `sep`: Specifies the delimiter (default: `,`).
- `header`: Row number to use as column headers (default: `0`).
- `names`: Custom column names.
- `dtype`: Specify column data types.

Example:
```python
df = pd.read_csv('users.csv', sep=',', dtype={'name': str, 'age': int})
```

---

## **5. Saving DataFrame to Database**
### `to_sql` Method:
pandas provides the `to_sql` method to save a DataFrame to a database table.

### Parameters:
- `name`: Name of the database table.
- `con`: Connection to the database.
- `if_exists`:
  - `fail`: Raises an error if the table exists.
  - `replace`: Drops the table and creates a new one.
  - `append`: Adds new rows to the existing table.
- `index`: Whether to write DataFrame index as a column.

### Example:
```python
df.to_sql('users', con=engine, if_exists='append', index=False)
```

---

## **6. SQLAlchemy Models**
SQLAlchemy uses Python classes to define database tables.

### Defining a Model:
```python
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
```

### Creating Tables:
The `create_all` method generates database tables for all defined models:
```python
Base.metadata.create_all(engine)
```

---

## **7. Bulk Data Insertion**
### Why Use Bulk Operations?
- Efficient for inserting large datasets.
- Minimizes database connection overhead.

### Using pandas `to_sql`:
```python
df.to_sql('users', con=engine, if_exists='append', index=False)
```

### Using SQLAlchemy Bulk Insert:
```python
users = [User(name='Alice', age=25), User(name='Bob', age=30)]
session.add_all(users)
session.commit()
```

---

## **8. Verifying Data in the Database**
### Querying Data:
Use SQLAlchemy’s ORM to fetch data:
```python
users = session.query(User).all()
for user in users:
    print(user)
```

### Raw SQL Queries:
For advanced operations, use `engine.execute`:
```python
result = engine.execute("SELECT * FROM users")
for row in result:
    print(row)
```

---

## **9. Common Use Cases**
### 9.1. Data Cleaning
Before saving the DataFrame, clean the data:
```python
df['age'] = df['age'].fillna(0)  # Replace NaN with 0
df['name'] = df['name'].str.strip()  # Remove extra spaces
```

### 9.2. Handling Duplicates
Drop duplicate rows:
```python
df = df.drop_duplicates()
```

### 9.3. Data Transformation
Apply transformations:
```python
df['age_category'] = df['age'].apply(lambda x: 'Adult' if x >= 18 else 'Minor')
```

---

## **10. Best Practices**
1. **Validate Data**:
   - Ensure the DataFrame matches the database schema.
2. **Error Handling**:
   - Wrap database operations in `try-except` blocks.
3. **Performance**:
   - Use bulk operations for large datasets.
4. **Avoid Overwriting**:
   - Use `if_exists='append'` to prevent accidental data loss.

---

## **11. Example Workflow**
Here’s a complete workflow:
1. Define the database connection and model:
   ```python
   from sqlalchemy import create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   engine = create_engine('sqlite:///example.db')
   Base = declarative_base()

   class User(Base):
       __tablename__ = 'users'
       id = Column(Integer, primary_key=True)
       name = Column(String)
       age = Column(Integer)

   Base.metadata.create_all(engine)
   ```
2. Load data from CSV:
   ```python
   import pandas as pd
   df = pd.read_csv('users.csv')
   ```
3. Save to database:
   ```python
   df.to_sql('users', con=engine, if_exists='append', index=False)
   ```
4. Query the database:
   ```python
   session = sessionmaker(bind=engine)()
   users = session.query(User).all()
   for user in users:
       print(user)
   ```

---

## **12. Summary**
- **pandas** simplifies CSV data manipulation and transformation.
- **SQLAlchemy** integrates seamlessly with relational databases.
- Bulk operations like `to_sql` improve performance for large datasets.
- Always validate and clean data before saving to a database.

---
