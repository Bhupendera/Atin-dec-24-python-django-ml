# Jinja2 Templating in Flask

## Overview
Jinja2 is a modern and powerful templating engine for Python, integrated into Flask. It allows developers to generate dynamic HTML by embedding Python expressions and control structures directly within templates.

---

## Subtopic 1: What is Jinja2?

### Key Concepts
1. **Definition**:
   - Jinja2 is a templating engine used to create dynamic HTML pages.
   - It allows separation of logic (in Flask views) and presentation (in templates).

2. **Features of Jinja2**:
   - Supports template inheritance.
   - Provides control structures like loops and conditionals.
   - Allows custom filters and macros.

3. **How Jinja2 Works in Flask**:
   - Templates are stored in the `templates/` directory.
   - Flask renders templates using the `render_template` function.

---

## Subtopic 2: Embedding Variables in Templates

### Key Concepts
1. **Syntax**:
   - Use `{{ variable }}` to display a variable's value:
     ```html
     <h1>Welcome, {{ username }}</h1>
     ```

2. **Passing Variables from Flask**:
   - In the view:
     ```python
     @app.route("/")
     def home():
         return render_template("home.html", username="Alice")
     ```

3. **Default Behavior**:
   - If a variable is not passed, it will be treated as `None`.

---

## Subtopic 3: Control Structures in Jinja2

### Key Concepts
1. **Conditionals**:
   - Use `{% if %}` and `{% else %}` for conditional rendering:
     ```html
     {% if user.is_admin %}
         <p>Welcome, Admin!</p>
     {% else %}
         <p>Welcome, User!</p>
     {% endif %}
     ```

2. **Loops**:
   - Use `{% for %}` to iterate over lists or dictionaries:
     ```html
     <ul>
         {% for item in items %}
             <li>{{ item }}</li>
         {% endfor %}
     </ul>
     ```

3. **Break and Continue**:
   - Control loop behavior:
     ```html
     {% for item in items %}
         {% if item == "skip" %}
             {% continue %}
         {% endif %}
         <li>{{ item }}</li>
     {% endfor %}
     ```

---

## Subtopic 4: Template Inheritance

### Key Concepts
1. **Base Templates**:
   - Define a common structure in a base template:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>{% block title %}My Site{% endblock %}</title>
     </head>
     <body>
         {% block content %}{% endblock %}
     </body>
     </html>
     ```

2. **Extending Templates**:
   - Extend the base template in other templates:
     ```html
     {% extends "base.html" %}

     {% block title %}Home{% endblock %}
     {% block content %}
         <h1>Welcome to My Site</h1>
     {% endblock %}
     ```

---

## Subtopic 5: Filters and Custom Filters

### Key Concepts
1. **Built-in Filters**:
   - Modify data before rendering:
     ```html
     <p>{{ username | upper }}</p>
     ```

2. **Common Filters**:
   - `upper`: Converts text to uppercase.
   - `lower`: Converts text to lowercase.
   - `length`: Returns the length of a list or string.

3. **Creating Custom Filters**:
   - Register a custom filter in Flask:
     ```python
     @app.template_filter("reverse")
     def reverse_string(value):
         return value[::-1]
     ```
   - Use in templates:
     ```html
     <p>{{ "Flask" | reverse }}</p>
     ```

---