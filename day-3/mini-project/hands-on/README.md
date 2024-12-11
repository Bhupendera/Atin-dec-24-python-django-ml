### Hands-On Guide for Sharing Content on Your Website

---

### Introduction
This hands-on guide complements the conceptual overview, detailing every practical step required to build and implement the features of an interactive image bookmarking website. It covers model creation, form customization, admin configuration, JavaScript integration, and performance optimization.

---

### Step 1: Setting Up the Environment

#### 1.1 Install Dependencies
Ensure your environment is ready by installing the required packages:

```bash
pip install django
pip install easy-thumbnails
pip install requests
```

Optional (if using Redis for caching):

```bash
pip install redis django-redis
```

#### 1.2 Start a Django Project and App

```bash
django-admin startproject bookmark_project
cd bookmark_project
django-admin startapp images
```

Add `images` to the `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'images',
]
```

---

### Step 2: Building the Image Model

Create the `Image` model in `images/models.py`:

```python
from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
```

Run migrations to apply the model:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 3: Admin Configuration

Register the `Image` model in `images/admin.py`:

```python
from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'user', 'created']
    list_filter = ['created']
    search_fields = ['title', 'description']
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the development server and log in to the admin panel:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` to test the admin configuration.

---

### Step 4: Creating the Image Form

Create a form for submitting images in `images/forms.py`:

```python
from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url.lower().endswith(('.jpg', '.jpeg', '.png')):
            raise forms.ValidationError('The URL must point to a valid image file.')
        return url
```

---

### Step 5: Building Views and URLs

#### 5.1 Create Views
In `images/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageCreateForm
from .models import Image

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect(image.get_absolute_url())
    else:
        form = ImageCreateForm()
    return render(request, 'images/image/create.html', {'form': form})
```

#### 5.2 Add URL Patterns
In `images/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
]
```

Include these URLs in the project’s `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('images/', include('images.urls', namespace='images')),
]
```

---

### Step 6: Implementing JavaScript Bookmarklet

#### 6.1 Add JavaScript Code
Create a `static/js/bookmarklet.js` file:

```javascript
(function() {
    var script = document.createElement('script');
    script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js';
    script.onload = function() {
        $('img').click(function(e) {
            e.preventDefault();
            alert('Image selected: ' + $(this).attr('src'));
        });
    };
    document.head.appendChild(script);
})();
```

#### 6.2 Generate the Bookmarklet
Create a view to generate the bookmarklet:

```python
from django.shortcuts import render

@login_required
def bookmarklet(request):
    return render(request, 'images/bookmarklet.html')
```

Add the template `templates/images/bookmarklet.html`:

```html
<a href="javascript:(function(){var script=document.createElement('script');script.src='https://example.com/static/js/bookmarklet.js';document.body.appendChild(script);})();">Bookmark Images</a>
```

---

### Step 7: Adding Thumbnails with Easy Thumbnails

Configure `easy-thumbnails` in `settings.py`:

```python
THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (100, 100), 'crop': True},
        'large': {'size': (800, 800), 'crop': False},
    },
}
```

Update the image model’s `image` field to integrate thumbnail generation:

```python
from easy_thumbnails.fields import ThumbnailerImageField

image = ThumbnailerImageField(upload_to='images/%Y/%m/%d/')
```

---

### Step 8: Adding Infinite Scroll

#### 8.1 Update the List View
Modify the image list view to support pagination in `views.py`:

```python
from django.core.paginator import Paginator

def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)  # 8 images per page
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, 'images/image/list.html', {'images': images})
```

#### 8.2 Add Infinite Scroll JavaScript
Include the following JavaScript in `list.html`:

```javascript
let page = 1;
window.onscroll = function() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        page++;
        fetch('/images/list/?page=' + page)
            .then(response => response.text())
            .then(html => {
                document.querySelector('#image-container').innerHTML += html;
            });
    }
};
```

---