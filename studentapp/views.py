from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    students = Student.objects.all()    
    return render(request, "home.html", {"students": students})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")

        student = Student(name=name, age=age, email=email, address=address)
        student.save()
        return redirect("home")
        
    return render(request, "add.html")

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.email = request.POST.get("email")
        student.address = request.POST.get("address")
        student.save()
        return redirect("home")
        
    return render(request, "edit.html", {"student": student})

# MAKE SURE THIS FUNCTION IS EXACTLY AT THE BOTTOM
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect("home")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
