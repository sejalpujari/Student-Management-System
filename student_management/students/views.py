from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Student 
def base(request):
    return render(request, 'base.html')
def student_list(request): 
    students = Student.objects.all() 
    return render(request, 'student_list.html', {'students': students})
def student_add(request): 
    if request.method == 'POST': 
# Extract data from the form 
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name') 
        email = request.POST.get('email') 
        date_of_birth = request.POST.get('date_of_birth') 
        grade = request.POST.get('grade') 
        address = request.POST.get('address') 
 
        # Create a new student 
        Student.objects.create( 
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            date_of_birth=date_of_birth, 
            grade=grade, 
            address=address 
        ) 
        # Redirect to the student list after saving 
        return redirect('student-list') 
 
    # If GET request, render the form 
    return render(request, 'student_form.html') 
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from .models import Student

def student_edit(request, pk):
    # Fetch the student by primary key (ID)
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        # Get form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        date_of_birth_str = request.POST.get('date_of_birth')  # Ensure format dd-mm-yyyy
        grade = request.POST.get('grade')
        address = request.POST.get('address')

        # Convert date_of_birth to datetime.date if available
        if date_of_birth_str:
            try:
                date_of_birth = datetime.strptime(date_of_birth_str, '%d-%m-%Y').date()
            except ValueError:
                date_of_birth = None  # Handle the case if the date format is incorrect
        else:
            date_of_birth = student.date_of_birth  # Preserve previous date if empty

        # Update the student details
        student.first_name = first_name
        student.last_name = last_name
        student.email = email
        student.date_of_birth = date_of_birth
        student.grade = grade
        student.address = address

        # Save changes to the database
        student.save()

        # Redirect to the student list view
        return redirect('student-list')

    # Render the form with existing data
    return render(request, 'student_form.html', {'student': student})

def student_delete(request, pk): 
    # Fetch the student by primary key (ID) 
    student = get_object_or_404(Student, pk=pk) 
 
    if request.method == 'POST': 
        student.delete()  # Delete the student record 
        return redirect('student-list') 
 
    # Render the delete confirmation page 
    return render(request, 'student_confirm_delete.html', {'student': student})