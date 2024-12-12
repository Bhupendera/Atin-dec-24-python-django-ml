from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

def index(request):
    return render(request, 'index.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        department = request.POST['department']
        salary = request.POST['salary']
        hire_date = request.POST['hire_date']
        Employee.objects.create(
            name=name,
            email=email,
            date_of_birth=date_of_birth,
            department=department,
            salary=salary,
            hire_date=hire_date
        )
        return redirect('employee_list')
    return render(request, 'employee_form.html')

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.date_of_birth = request.POST['date_of_birth']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.hire_date = request.POST['hire_date']
        employee.save()
        return redirect('employee_list')
    else:
        # Format the date to YYYY-MM-DD
        employee.date_of_birth = employee.date_of_birth.strftime('%Y-%m-%d')
        employee.hire_date = employee.hire_date.strftime('%Y-%m-%d')

    return render(request, 'employee_form.html', {'employee': employee})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})
