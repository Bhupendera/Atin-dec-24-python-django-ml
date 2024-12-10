# Django Concepts

## **1. Introduction to Django**
Django is a high-level Python web framework designed for rapid development and clean, pragmatic design. It provides tools and features to simplify web development.

### Key Features:
1. **MTV Architecture**:
   - **Model**: Handles data and business logic.
   - **Template**: Manages the presentation layer (HTML).
   - **View**: Connects Models and Templates by processing requests and returning responses.
2. **Built-in Admin Interface**:
   - Auto-generated interface for managing application data.
3. **ORM (Object-Relational Mapping)**:
   - Simplifies database interactions using Python objects.
4. **Scalability**:
   - Supports scalable and robust applications.

---

## **2. Project Structure Overview**
When you create a Django project, the directory structure looks like this:

```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

### Key Files:
1. **manage.py**:
   - Command-line utility for managing the project.
   - Handles migrations, server startup, creating users, etc.
2. **settings.py**:
   - Centralized configuration for the project.
   - Includes installed apps, middleware, databases, static files, and more.
3. **urls.py**:
   - Maps URLs to views.
4. **wsgi.py** and **asgi.py**:
   - Interfaces for deploying the project in WSGI or ASGI-compatible servers.

---

## **3. Applications in Django**
Django projects are divided into smaller components called **apps**. Each app is a self-contained module that provides specific functionality.

### Creating an App:
- Use `startapp` to create a new app.
- Apps must be added to `INSTALLED_APPS` in `settings.py`.

---

## **4. Models**
Models define the structure of your data and represent database tables. Each model is a Python class that inherits from `django.db.models.Model`.

### Key Concepts:
1. **Fields**:
   - Represent columns in the database.
   - Example: `CharField`, `TextField`, `DateTimeField`.
2. **Methods**:
   - `__str__`: Defines the string representation of an object.
   - `get_absolute_url`: Returns the URL for an object.

### Example:
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

---

## **5. Migrations**
Migrations are Django’s way of propagating changes to models into the database schema.

### Workflow:
1. **Creating Migrations**:
   - `makemigrations`: Generates migration files for model changes.
2. **Applying Migrations**:
   - `migrate`: Applies migration files to the database.
3. **Viewing SQL**:
   - `sqlmigrate`: Displays the SQL that will be executed by a migration.

---

## **6. QuerySet and ORM**
The ORM allows interaction with the database using Python objects.

### Key Operations:
1. **Create**:
   - Add a new record to the database.
   - Example: `Post.objects.create(title="Sample", body="Content")`.
2. **Retrieve**:
   - Fetch all or specific records.
   - Example: `Post.objects.all()`, `Post.objects.get(pk=1)`.
3. **Filter**:
   - Query records based on conditions.
   - Example: `Post.objects.filter(title__icontains="Sample")`.
4. **Update**:
   - Modify existing records.
5. **Delete**:
   - Remove records from the database.

### Lazy Evaluation:
- QuerySets are not evaluated until explicitly needed.
- This improves performance and reduces database load.

---

## **7. URL Configuration**
URLs in Django are mapped to views using the `urls.py` file.

### Structure:
1. **Root `urls.py`**:
   - Includes app-specific URLs.
   - Example:
     ```python
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('blog.urls')),
     ]
     ```
2. **App `urls.py`**:
   - Defines URLs for the app.
   - Example:
     ```python
     urlpatterns = [
         path('', views.post_list, name='post_list'),
     ]
     ```

---

## **8. Views**
Views are Python functions or classes that handle HTTP requests and return HTTP responses.

### Types of Views:
1. **Function-Based Views (FBVs)**:
   - Example:
     ```python
     def post_list(request):
         posts = Post.objects.all()
         return render(request, 'blog/post_list.html', {'posts': posts})
     ```
2. **Class-Based Views (CBVs)**:
   - Offer built-in functionality for common patterns.
   - Example: `ListView`, `DetailView`.

---

## **9. Templates**
Templates define the HTML structure for the application.

### Template Tags:
- `{% for %}`, `{% if %}`: Control structures.
- `{{ variable }}`: Outputs variables.

### Template Inheritance:
- Base templates define the layout, while child templates extend and customize them.

---

## **10. Static Files and Media**
1. **Static Files**:
   - Include CSS, JavaScript, and images.
   - Use `{% static 'path/to/file.css' %}` to reference static files in templates.
2. **Media Files**:
   - User-uploaded content.

---

## **11. Admin Interface**
Django provides an admin interface for managing data.

### Customization:
- Register models in `admin.py`.
- Customize admin display using fields, filters, and search capabilities.

Example:
```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    search_fields = ('title', 'body')
```

---

## **12. Django Shell**
The shell provides an interactive Python environment to interact with the database.

### Key Commands:
- Start the shell:
  ```bash
  python manage.py shell
  ```
- Common operations:
  - Create objects: `Post.objects.create(title="Sample")`.
  - Retrieve objects: `Post.objects.all()`.
  - Filter objects: `Post.objects.filter(title__icontains="Sample")`.

---

## **13. Management Commands**
Django provides several built-in commands:
1. `runserver`: Starts the development server.
2. `migrate`: Applies migrations.
3. `makemigrations`: Creates migration files.
4. `createsuperuser`: Creates an admin user.
5. `shell`: Opens an interactive shell.

---

## **14. Summary**
- Project and app structures.
- Models, migrations, and ORM operations.
- Views, templates, and URL mapping.
- Admin interface and management commands.

---
