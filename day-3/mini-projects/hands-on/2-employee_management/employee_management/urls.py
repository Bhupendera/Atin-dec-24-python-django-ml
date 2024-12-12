from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')),
    path('auth/', include('auth_app.urls')),
    path('', home_view, name='home'),  # Add this line for the home page
]



handler404 = 'employee_management.views.custom_404'
handler500 = 'employee_management.views.custom_500'
