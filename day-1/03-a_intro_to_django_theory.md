# Introduction to Django Framework

## Overview
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It provides built-in tools for handling database interactions, user authentication, and dynamic web pages, making it one of the most popular frameworks for web development.

---

## Subtopic 1: What is Django?

### Key Concepts
1. **Definition**:
   Django is a Python-based web framework that simplifies web application development by providing built-in tools for handling common tasks such as database interaction, templating, and routing.

2. **Why Django?**
   - **Fast Development**: Built-in features reduce development time.
   - **Secure**: Includes protection against common web attacks like SQL injection, XSS, CSRF, etc.
   - **Scalable**: Suitable for small projects to large, high-traffic applications.

3. **Django’s Philosophy**:
   - **Don’t Repeat Yourself (DRY)**: Avoid duplication in code.
   - **Explicit is Better than Implicit**: Clear and transparent code.

---

## Subtopic 2: Setting Up Django

### Key Concepts
1. **Installation**:
   - Install Django using pip:
     ```bash
     pip install django
     ```

2. **Creating a Project**:
   - A project in Django is a collection of settings and configurations for a web application.
   - Create a new project:
     ```bash
     django-admin startproject project_name
     ```

3. **Project Structure**:
   - Key files in a project:
     - `manage.py`: Utility for interacting with the project.
     - `settings.py`: Configuration for the project (e.g., database settings).
     - `urls.py`: Defines URL routing.

4. **Running the Development Server**:
   - Start the server:
     ```bash
     python manage.py runserver
     ```
   - Access the application at `http://127.0.0.1:8000`.

---

## Subtopic 3: Creating a Django App

### Key Concepts
1. **What is an App?**
   - An app is a modular component of a Django project that performs specific functionalities, such as a blog, user management, or e-commerce.

2. **Creating an App**:
   - Create an app using the `startapp` command:
     ```bash
     python manage.py startapp app_name
     ```

3. **Registering the App**:
   - Add the app to the `INSTALLED_APPS` list in `settings.py`:
     ```python
     INSTALLED_APPS = [
         ...,
         'app_name',
     ]
     ```

4. **Directory Structure**:
   - Key files in an app:
     - `models.py`: Defines database models.
     - `views.py`: Handles logic and renders responses.
     - `urls.py`: Routes URLs to views.

---

## Hands-On Activities
Refer to the file: `03_intro_to_django_hands_on.md`
