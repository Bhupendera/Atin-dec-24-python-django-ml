### **1. Retrieve `id` After Insertion**

#### Example:
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define database connection and session
engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Define the model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

# Insert a record and retrieve the id
new_user = User(name='Alice', age=25)
session.add(new_user)
session.commit()  # Commit the transaction to generate the id

print(f"Inserted User ID: {new_user.id}")
```

---

### **2. Bulk Insert and Retrieve IDs**
If you’re inserting multiple records, you can retrieve their `id` values after committing the session.

#### Example:
```python
users = [
    User(name='Bob', age=30),
    User(name='Charlie', age=35),
]

session.add_all(users)
session.commit()

# Retrieve IDs
for user in users:
    print(f"Inserted User: {user.name}, ID: {user.id}")
```

---

### **3. Using `flush` Before `commit`**
In some cases, you might want to retrieve the `id` without committing the transaction. You can use `flush` to send changes to the database without committing them.

#### Example:
```python
new_user = User(name='Diana', age=28)
session.add(new_user)
session.flush()  # Send to the database but don't commit

print(f"Inserted User ID (before commit): {new_user.id}")

session.commit()  # Commit the transaction
```

---

### **4. Raw SQL Insertion**
When using raw SQL for insertion, you can retrieve the `id` using the database cursor.

#### Example:
```python
from sqlalchemy import text

# Insert and fetch the id using RETURNING clause
result = engine.execute(text(
    "INSERT INTO users (name, age) VALUES (:name, :age) RETURNING id"
), {"name": "Eve", "age": 22})

inserted_id = result.fetchone()[0]
print(f"Inserted User ID: {inserted_id}")
```

---

### **5. Important Notes**
1. **Primary Key Autogeneration**:
   - The `id` value is generated automatically if your database is configured with an auto-increment primary key.
   - Ensure the column is defined as `primary_key=True`.

2. **Session Commit/Flush**:
   - `commit`: Saves the transaction and makes changes permanent.
   - `flush`: Sends the changes to the database but doesn’t finalize the transaction.

3. **Batch Inserts with Bulk Save**:
   - If you use bulk methods like `bulk_save_objects`, you might not get the `id` values immediately since these methods bypass ORM features.

---

### **6. Summary**
- Use `session.commit()` to retrieve `id` after inserting a record.
- Use `session.flush()` to get the `id` before committing.
- For raw SQL, use `RETURNING id` or fetch the auto-generated value from the cursor.
