import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database engine and session
engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Define the declarative base
Base = declarative_base()

# Define the model for the database table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# Create the users table
Base.metadata.create_all(engine)

# Function to read a CSV file
def read_csv(file_path):
    print(f"Reading data from {file_path}...")
    df = pd.read_csv(file_path)
    print("CSV Data:\n", df)
    return df

# Function to save DataFrame to database
def save_to_db(df, table_name):
    print(f"Saving DataFrame to database table '{table_name}'...")
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print("Data saved to database.")

print ("__name__: ", __name__)

if __name__ == '__main__':
    # Example CSV file
    csv_file_path = 'users.csv'

    # Step 1: Read CSV into pandas DataFrame
    df = read_csv(csv_file_path)

    # Step 2: Save DataFrame to database
    save_to_db(df, 'users')

    # Verify data insertion
    print("Verifying data in the database:")
    users = session.query(User).all()
    for user in users:
        print(user)
