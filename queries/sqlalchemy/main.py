from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the database engine and session
engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Define the declarative base
Base = declarative_base()

# Define Models
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    posts = relationship('Post', back_populates='user')

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post(title='{self.title}', user_id={self.user_id})>"

# Create all tables
def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created.")

# Add sample users
def add_users():
    users = [
        User(name="Alice", age=25),
        User(name="Bob", age=30),
        User(name="Charlie", age=35)
    ]
    session.add_all(users)
    session.commit()
    print("Users added.")

# Query all users
def query_users():
    users = session.query(User).all()
    for user in users:
        print(user)

# Add posts for a user
def add_posts():
    user = session.query(User).filter_by(name="Alice").first()
    if user:
        posts = [
            Post(title="Alice's First Post", user=user),
            Post(title="Alice's Second Post", user=user)
        ]
        session.add_all(posts)
        session.commit()
        print(f"Posts added for {user.name}.")

# Query posts and their users
def query_posts():
    posts = session.query(Post).all()
    for post in posts:
        print(f"Post: {post.title}, User: {post.user.name}")

# Update user information
def update_user():
    user = session.query(User).filter_by(name="Bob").first()
    if user:
        user.age = 32
        session.commit()
        print(f"User {user.name}'s age updated to {user.age}.")

# Delete a user
def delete_user():
    user = session.query(User).filter_by(name="Charlie").first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user.name} deleted.")

# Drop all tables
def drop_tables():
    Base.metadata.drop_all(engine)
    print("Tables dropped.")

if __name__ == '__main__':
    # Menu for running examples
    print("SQLAlchemy Examples")
    print("1. Create Tables")
    print("2. Add Users")
    print("3. Query Users")
    print("4. Add Posts")
    print("5. Query Posts")
    print("6. Update User")
    print("7. Delete User")
    print("8. Drop Tables")

    choice = input("Enter the example number to run: ").strip()

    if choice == '1':
        create_tables()
    elif choice == '2':
        add_users()
    elif choice == '3':
        query_users()
    elif choice == '4':
        add_posts()
    elif choice == '5':
        query_posts()
    elif choice == '6':
        update_user()
    elif choice == '7':
        delete_user()
    elif choice == '8':
        drop_tables()
    else:
        print("Invalid choice. Exiting.")


# How to use:
# pip install -r requirements.txt
# python main.py
