# Introduction to Flask

## Overview
Flask is a lightweight and flexible Python web framework designed for simplicity and rapid development. It follows a microframework approach, providing essential tools for building web applications while allowing developers to extend functionality as needed.

---

## Subtopic 1: What is Flask?

### Key Concepts
1. **Definition**:
   - Flask is a minimalistic web framework based on WSGI (Web Server Gateway Interface).
   - Developed by Armin Ronacher, it provides basic tools to build web applications.

2. **Features of Flask**:
   - Lightweight and modular.
   - Built-in development server and debugger.
   - Flexible routing.
   - Support for extensions (e.g., Flask-SQLAlchemy, Flask-WTF).
   - RESTful request handling.

3. **When to Use Flask**:
   - Ideal for small to medium-sized applications.
   - Suitable for applications requiring high flexibility and customization.

---

## Subtopic 2: Setting Up Flask

### Key Concepts
1. **Installing Flask**:
   - Flask can be installed via pip:
     ```bash
     pip install flask
     ```

2. **Creating a Flask Application**:
   - A minimal Flask application:
     ```python
     from flask import Flask

     app = Flask(__name__)

     @app.route("/")
     def home():
         return "Welcome to Flask!"

     if __name__ == "__main__":
         app.run(debug=True)
     ```

3. **Running the Application**:
   - Save the file as `app.py` and run:
     ```bash
     python app.py
     ```
   - Access the application at `http://127.0.0.1:5000`.

---

## Subtopic 3: URL Routing and Handling Requests

### Key Concepts
1. **URL Routing**:
   - Flask uses decorators to define URL routes:
     ```python
     @app.route("/")
     def home():
         return "Home Page"
     ```

2. **Dynamic Routing**:
   - Include variables in routes:
     ```python
     @app.route("/user/<username>")
     def user_profile(username):
         return f"User: {username}"
     ```

3. **Request Handling**:
   - Access query parameters:
     ```python
     from flask import request

     @app.route("/search")
     def search():
         query = request.args.get("q")
         return f"Search query: {query}"
     ```

---

## Subtopic 4: Rendering HTML Templates

### Key Concepts
1. **Template Rendering**:
   - Flask uses the **Jinja2** templating engine.
   - Example:
     ```python
     from flask import render_template

     @app.route("/")
     def home():
         return render_template("home.html")
     ```

2. **Dynamic HTML**:
   - Use placeholders in HTML:
     ```html
     <h1>Welcome, {{ username }}</h1>
     ```

3. **Passing Variables to Templates**:
   - Pass data to templates:
     ```python
     @app.route("/user/<username>")
     def user_profile(username):
         return render_template("profile.html", username=username)
     ```

---
