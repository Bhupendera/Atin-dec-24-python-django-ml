from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee

@login_required
def employee_list(request):
    employees = Employee.objects.select_related('created_by').all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


@login_required
def employee_create(request):
    if request.method == 'POST':
        # Collect data from the form submission
        name = request.POST['name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        department = request.POST['department']
        salary = request.POST['salary']
        hire_date = request.POST['hire_date']

        # Create a new employee record
        Employee.objects.create(
            name=name,
            email=email,
            date_of_birth=date_of_birth,
            department=department,
            salary=salary,
            hire_date=hire_date,
            created_by=request.user
        )
        return redirect('employee_list')
    return render(request, 'employees/employee_form.html', {'employee': None})

@login_required
def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        # Update the employee record with new data
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.date_of_birth = request.POST['date_of_birth']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.hire_date = request.POST['hire_date']
        employee.save()
        return redirect('employee_list')
    return render(request, 'employees/employee_form.html', {'employee': employee})

@login_required
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        # Delete the employee record
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})


@login_required
def employee_details(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employees/employee_details.html', {'employee': employee})
