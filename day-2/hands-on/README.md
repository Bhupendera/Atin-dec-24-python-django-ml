## **1. Setting Up the Environment**
### Install Python
1. Install Python from the [official website](https://www.python.org/).
2. Verify the installation:
   ```bash
   python --version
   ```
   Example output:
   ```
   Python 3.12.x
   ```

### Create a Virtual Environment
1. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```
2. Activate the environment:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```

### Install Django
1. Install Django:
   ```bash
   pip install django
   ```
2. Verify the installation:
   ```bash
   python -m django --version
   ```
   Example output:
   ```
   Django 5.0
   ```

---

## **2. Starting a Django Project**
1. Create a Django project:
   ```bash
   django-admin startproject myproject
   ```
2. Navigate to the project directory:
   ```bash
   cd myproject
   ```

### Project Structure
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

---

## **3. Creating and Applying Migrations**
1. Initial migrations:
   ```bash
   python manage.py makemigrations
   ```
2. Create migrations for a new model:
   ```bash
   python manage.py migrate
   ```
3. Create new blog app
   ```bash
   python manage.py startapp blog
   ```
#### - Note: Please do an entry for app in settings.py with the name - blog

---

## **4. Defining Models**
1. Open `blog/models.py` and define a `Post` model:
   ```python
   from django.db import models

   class Post(models.Model):
       title = models.CharField(max_length=200)
       slug = models.SlugField(unique=True)
       body = models.TextField()
       created = models.DateTimeField(auto_now_add=True)
       updated = models.DateTimeField(auto_now=True)

       def __str__(self):
           return self.title
   ```

2. Migrations
   ```bash
   python manage.py makemigrations
   ```

3. View the SQL of a migration:
   ```bash
   python manage.py sqlmigrate blog 0001*
   ```
   
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```


---

## **5. Using the Django Shell**
### Open the Shell
Start an interactive session:
```bash
python manage.py shell
```

### Object Creation
1. Import the `Post` model:
   ```python
   from blog.models import Post
   ```
2. Create a new object:
   ```python
   post = Post.objects.create(
       title="First Post",
       slug="first-post",
       body="This is the body of the first post."
   )
   ```

### Retrieving Objects
1. Retrieve all objects:
   ```python
   Post.objects.all()
   ```
2. Retrieve by primary key:
   ```python
   Post.objects.get(pk=1)
   ```

### Filtering Objects
1. Filter objects:
   ```python
   Post.objects.filter(title__icontains="Post")
   ```
2. Use field lookups:
   ```python
   Post.objects.filter(slug__iexact="first-post")
   ```

### Advanced Queries
1. Chain filters:
   ```python
   Post.objects.filter(title__icontains="Post", body__icontains="body")
   ```
2. Order objects:
   ```python
   Post.objects.order_by('created')
   ```

---

## **6. Admin Interface**
1. Register the `Post` model in `blog/admin.py`:
   ```python
   from django.contrib import admin
   from .models import Post

   admin.site.register(Post)
   ```
2. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

3. Run server
   ```bash
   python manage.py runserver
   ```


4. Log in to the admin panel:
   ```
   http://127.0.0.1:8000/admin/
   ```

---

## **7. QuerySet Operations**
1. Count objects:
   ```python
   Post.objects.count()
   ```
2. Check for existence:
   ```python
   Post.objects.exists()
   ```
3. Exclude objects:
   ```python
   Post.objects.exclude(title__icontains="Post")
   ```
4. Debug queries:
   ```bash
   python manage.py debugsqlshell
   ```

---

## **8. Creating Views**
1. Define a view in `blog/views.py`:
   ```python
   from django.shortcuts import render
   from .models import Post

   def post_list(request):
       posts = Post.objects.all()
       return render(request, 'blog/post_list.html', {'posts': posts})
   ```
2. Add URL patterns:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.post_list, name='post_list'),
   ]
   ```

---

## **9. Creating Templates**
1. Create `templates/blog/post_list.html`:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Blog</title>
   </head>
   <body>
       <h1>Blog Posts</h1>
       {% for post in posts %}
           <h2>{{ post.title }}</h2>
           <p>{{ post.body }}</p>
           <small>Created: {{ post.created }}</small>
           <hr>
       {% endfor %}
   </body>
   </html>
   ```

---

## **10. Management Commands Summary**
### Frequently Used Commands:
- Run the development server:
  ```bash
  python manage.py runserver
  ```
- Create migrations:
  ```bash
  python manage.py makemigrations
  ```
- Apply migrations:
  ```bash
  python manage.py migrate
  ```
- Start the shell:
  ```bash
  python manage.py shell
  ```
- Create a superuser:
  ```bash
  python manage.py createsuperuser
  ```

---

## **11. Summary**
- Installed Python and Django.
- Set up a project and application.
- Defined a `Post` model and worked with QuerySets.
- Created views, templates, and mapped URLs.
- Used Django admin and explored shell commands.

---
