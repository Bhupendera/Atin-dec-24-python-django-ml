# **Migrating Tables Using Alembic with SQLAlchemy**

Alembic is the recommended tool for handling database migrations when using **SQLAlchemy**. It provides an easy way to manage schema changes and generate migration scripts, similar to Django's `manage.py migrate`.

### **1. Installing Alembic**

First, you need to install **Alembic**. You can install it via pip:

```bash
pip install alembic
```

### **2. Initializing Alembic**

To initialize Alembic in your project, navigate to the directory where your project is located and run the following command:

```bash
alembic init alembic
```

This will create an `alembic` directory with the following structure:

```
alembic/
    env.py          # The script that sets up the migration context.
    script.py.mako  # The template for the migration scripts.
    versions/       # The directory where migration scripts will be stored.
alembic.ini         # Alembic configuration file.
```

### **3. Configuring Alembic**

Next, you need to configure Alembic to work with your SQLAlchemy database. In the `alembic.ini` file, find the `sqlalchemy.url` section and set the database URL to point to your database.

For example, for SQLite:

```ini
sqlalchemy.url = sqlite:///example.db
```


Now, edit the `env.py` file in the `alembic/` directory. You need to import your SQLAlchemy `Base` object, which contains all your model definitions.

In `env.py`:

```python
from myproject import Base  # Import your Base class, which is used to create models.
from myproject.models import *  # Import all models to include them in migrations
```

Make sure that `Base` is correctly set up to reflect your SQLAlchemy models. Typically, `Base` is created by inheriting from `declarative_base` in SQLAlchemy:

```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

### **4. Creating Migrations**

Once Alembic is set up, you can generate migration scripts to reflect changes in your database schema.

#### **4.1 Generating the First Migration Script**

To create a migration script based on the current state of your models, run:

```bash
alembic revision --autogenerate -m "Initial migration"
```

This command will compare the current database schema with the models and generate a migration script inside the `alembic/versions/` directory.

You can inspect the generated migration file, which will contain the necessary SQL statements to apply the changes.

#### **4.2 Applying Migrations**

Once you've reviewed the migration script, you can apply the migration to the database by running:

```bash
alembic upgrade head
```

This command applies all the migrations that haven't been applied yet, updating your database schema.

### **5. Managing Migrations**

#### **5.1 Creating Additional Migrations**

As you modify your models, you can create new migration scripts with:

```bash
alembic revision --autogenerate -m "Add new field to Author model"
```

This will detect changes like added fields, removed columns, or changes in relationships and generate a migration script accordingly.

#### **5.2 Downgrading Migrations**

If you need to undo a migration, you can downgrade to a previous migration with:

```bash
alembic downgrade -1
```

This command will revert the most recent migration. You can also downgrade to a specific migration version:

```bash
alembic downgrade <version_number>
```

You can find the version number in the migration script file name (e.g., `12345_add_column_to_author.py`).

#### **5.3 Show Current Version**

To check which migration is currently applied to your database, you can run:

```bash
alembic current
```

### **6. Example Usage**

Below is an example of a basic SQLAlchemy model and how it integrates with Alembic for migrations.

#### **6.1 Defining SQLAlchemy Models**

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(String)
```

#### **6.2 Generating the First Migration**

After setting up your models, generate the migration script:

```bash
alembic revision --autogenerate -m "Create authors table"
```

This will create a migration file with the necessary SQL to create the `authors` table.

#### **6.3 Applying the Migration**

Apply the migration to the database:

```bash
alembic upgrade head
```

---
