# User Authentication in Django

## Overview
User authentication is a crucial aspect of web applications. Django provides a built-in authentication framework to handle tasks like user registration, login, logout, and permissions.

---

## Subtopic 1: Understanding Django's Authentication Framework

### Key Concepts
1. **What is Django Authentication?**
   - A system for identifying users and verifying their credentials.
   - Includes features for login, logout, password management, and user permissions.

2. **Default User Model**:
   - Django includes a built-in `User` model with fields like `username`, `email`, `password`, `first_name`, and `last_name`.

3. **Key Components**:
   - **Middleware**: Handles session management.
   - **Views**: Pre-built views for login/logout functionality.
   - **Forms**: Pre-built forms like `AuthenticationForm` for validating user input.

---

## Subtopic 2: Implementing User Registration

### Key Concepts
1. **UserCreationForm**:
   - Django provides a pre-built form for creating new users.
   - Example:
     ```python
     from django.contrib.auth.forms import UserCreationForm
     from django.shortcuts import render, redirect

     def register(request):
         if request.method == "POST":
             form = UserCreationForm(request.POST)
             if form.is_valid():
                 form.save()
                 return redirect("login")
         else:
             form = UserCreationForm()
         return render(request, "register.html", {"form": form})
     ```

2. **Password Hashing**:
   - User passwords are securely hashed using Django's authentication system.
   - Supported algorithms: PBKDF2 (default), Argon2, bcrypt.

3. **Adding Custom Fields**:
   - Extend the `UserCreationForm` to include additional fields:
     ```python
     from django.contrib.auth.forms import UserCreationForm
     from django import forms
     from django.contrib.auth.models import User

     class CustomUserCreationForm(UserCreationForm):
         email = forms.EmailField()

         class Meta:
             model = User
             fields = ["username", "email", "password1", "password2"]
     ```

---

## Subtopic 3: Login and Logout Functionality

### Key Concepts
1. **LoginView**:
   - Django’s built-in `LoginView` handles user login.
   - Example:
     ```python
     from django.contrib.auth.views import LoginView

     class CustomLoginView(LoginView):
         template_name = "login.html"
     ```

2. **LogoutView**:
   - `LogoutView` is used for logging out users.
   - Example:
     ```python
     from django.contrib.auth.views import LogoutView

     class CustomLogoutView(LogoutView):
         next_page = "login"
     ```

3. **Session Management**:
   - Django automatically manages user sessions and cookies for login/logout functionality.

---

