# SQLAlchemy

## **1. Introduction to SQLAlchemy**
SQLAlchemy is a Python SQL toolkit and Object-Relational Mapping (ORM) library. It provides a flexible system to interact with databases using Python code.

### Key Components:
1. **Core**: Provides SQL expression language for constructing SQL queries.
2. **ORM (Object-Relational Mapper)**: Maps Python classes to database tables.

---

## **2. Installation**
To install SQLAlchemy, use:
```bash
pip install sqlalchemy
```

---

## **3. SQLAlchemy Concepts**
### 3.1 Engine
- The `Engine` is the starting point for SQLAlchemy.
- It manages the connection to the database.
- Example:
  ```python
  from sqlalchemy import create_engine
  engine = create_engine('sqlite:///example.db', echo=True)
  ```

### 3.2 Declarative Base
- Declarative base is the foundation for defining ORM models.
- Example:
  ```python
  from sqlalchemy.ext.declarative import declarative_base
  Base = declarative_base()
  ```

### 3.3 Session
- A `Session` manages interactions with the database.
- Example:
  ```python
  from sqlalchemy.orm import sessionmaker
  Session = sessionmaker(bind=engine)
  session = Session()
  ```

---

## **4. Defining Models**
Models are Python classes that define database tables.

### Example:
```python
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"
```

---

## **5. Working with Tables**
### Creating Tables with `create_all`
The `create_all` method generates all the tables defined in the ORM models. It does not recreate tables if they already exist.

### Explanation:
- `create_all` checks the `Base.metadata` for all defined models.
- It executes the SQL `CREATE TABLE` statements for those models.
- **Important**: It does not drop existing tables. Use `drop_all` if needed.

### Example:
```python
# Create tables based on all defined models
Base.metadata.create_all(engine)
```

---

## **6. Basic Operations**
### Adding Records
```python
new_user = User(name='Alice', age=25)
session.add(new_user)
session.commit()
```

### Querying Records
```python
# Get all users
users = session.query(User).all()
for user in users:
    print(user)

# Filter records
user = session.query(User).filter_by(name='Alice').first()
```

### Updating Records
```python
user = session.query(User).filter_by(name='Alice').first()
user.age = 30
session.commit()
```

### Deleting Records
```python
user = session.query(User).filter_by(name='Alice').first()
session.delete(user)
session.commit()
```

---

## **7. Relationships**
SQLAlchemy supports relationships between tables.

### One-to-Many Relationship
```python
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')

User.posts = relationship('Post', order_by=Post.id, back_populates='user')
```

---

## **8. Cheatsheet**
### Engine
```python
engine = create_engine('sqlite:///example.db', echo=True)
```

### Declarative Base
```python
Base = declarative_base()
```

### Session
```python
Session = sessionmaker(bind=engine)
session = Session()
```

### Basic Methods
| Method            | Purpose                                  |
|--------------------|------------------------------------------|
| `add(obj)`         | Add a new record to the session.         |
| `commit()`         | Save changes to the database.           |
| `query(model)`     | Query the database.                     |
| `filter_by(**kwargs)` | Filter query results by exact match.   |
| `delete(obj)`      | Delete a record from the database.      |

### Creating Tables
```python
Base.metadata.create_all(engine)
```

### Dropping Tables
```python
Base.metadata.drop_all(engine)
```

### Query Examples
```python
# Retrieve all records
session.query(User).all()

# Filter by a field
session.query(User).filter_by(name='Alice').first()

# Advanced filters
session.query(User).filter(User.age > 25).all()
```

---

## **9. Advanced Concepts**
### Transactions
SQLAlchemy sessions handle transactions automatically:
- `commit()`: Finalize a transaction.
- `rollback()`: Revert changes.

### Raw SQL Queries
You can execute raw SQL using `engine.execute`:
```python
result = engine.execute("SELECT * FROM users")
for row in result:
    print(row)
```

### Asynchronous ORM
For asynchronous operations, use SQLAlchemy's async API:
```python
from sqlalchemy.ext.asyncio import create_async_engine
async_engine = create_async_engine('sqlite+aiosqlite:///example.db')
```

---

## **10. Common Pitfalls**
1. **Forget to commit**:
   - Changes are not persisted unless `commit()` is called.
2. **Session conflicts**:
   - Use separate sessions for independent operations.
3. **Misuse of `create_all`**:
   - It doesn’t alter existing tables. Use migrations (e.g., Alembic) for schema changes.

---
