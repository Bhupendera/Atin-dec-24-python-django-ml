from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection and session
engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Define the declarative base
Base = declarative_base()

# Define the model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# Create the users table
Base.metadata.create_all(engine)

# Function to insert a single record and get the ID
def insert_single_record():
    new_user = User(name="Alice", age=25)
    session.add(new_user)
    session.commit()  # Commit the transaction
    print(f"Inserted User ID: {new_user.id}")

# Function to insert multiple records and get their IDs
def insert_multiple_records():
    users = [
        User(name="Bob", age=30),
        User(name="Charlie", age=35),
    ]
    session.add_all(users)
    session.commit()  # Commit the transaction
    for user in users:
        print(f"Inserted User: {user.name}, ID: {user.id}")

# Function to use flush to get the ID before commit
def insert_with_flush():
    new_user = User(name="Diana", age=28)
    session.add(new_user)
    session.flush()  # Send to the database but don't commit
    print(f"Inserted User ID (before commit): {new_user.id}")
    session.commit()  # Commit the transaction

# Function to use raw SQL and retrieve the ID
def insert_with_raw_sql():
    result = engine.execute(text(
        "INSERT INTO users (name, age) VALUES (:name, :age) RETURNING id"
    ), {"name": "Eve", "age": 22})
    inserted_id = result.fetchone()[0]
    print(f"Inserted User ID (via raw SQL): {inserted_id}")

# Function to verify data in the database
def verify_data():
    users = session.query(User).all()
    print("All Users in the Database:")
    for user in users:
        print(user)

if __name__ == '__main__':
    print("### Insert Single Record ###")
    insert_single_record()

    print("\n### Insert Multiple Records ###")
    insert_multiple_records()

    print("\n### Insert with Flush ###")
    insert_with_flush()

    print("\n### Insert with Raw SQL ###")
    insert_with_raw_sql()

    print("\n### Verify Data ###")
    verify_data()
