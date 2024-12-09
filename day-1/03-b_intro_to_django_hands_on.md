# Hands-On: Introduction to Django Framework

## Prerequisites
1. Install Python (3.x).
2. Install Django:
   ```bash
   pip install django
   ```

---

## Task 1: Setting Up a Django Project
1. Open a terminal and create a new Django project:
   ```bash
   django-admin startproject myproject
   cd myproject
   ```
2. Run the development server:
   ```bash
   python manage.py runserver
   ```
3. Open `http://127.0.0.1:8000` in a browser and verify the default Django welcome page.

---

## Task 2: Creating a Django App
1. Inside the project directory, create a new app:
   ```bash
   python manage.py startapp employees
   ```
2. Register the app in `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...,
       'employees',
   ]
   ```

---

## Task 3: Creating and Using Models
1. Define a model for `Employee` in `employees/models.py`:
   ```python
   from django.db import models

   class Employee(models.Model):
       name = models.CharField(max_length=100)
       age = models.IntegerField()
       department = models.CharField(max_length=50)

       def __str__(self):
           return self.name
   ```
2. Make migrations to prepare the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Add a record using the Django shell:
   ```bash
   python manage.py shell
   >>> from employees.models import Employee
   >>> Employee.objects.create(name='Alice', age=28, department='HR')
   >>> Employee.objects.all()
   ```

---

## Task 4: Creating Views and URL Routing
1. Define a view in `employees/views.py`:
   ```python
   from django.http import HttpResponse

   def index(request):
       return HttpResponse("Welcome to the Employees App!")
   ```
2. Create a `urls.py` file in the `employees` app:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```
3. Include the app URLs in the project’s `urls.py`:
   ```python
   from django.urls import include, path

   urlpatterns = [
       path('employees/', include('employees.urls')),
   ]
   ```
4. Run the server and visit `http://127.0.0.1:8000/employees`.
   ```bash
   python manage.py runserver
   ```

---

## Additional Exercises
1. Create another app for managing departments and link it to employees using a foreign key.
2. Create a database migration that adds an additional field (e.g., `email`) to the `Employee` model.
3. Create a view that displays all employees in a simple HTML template.
