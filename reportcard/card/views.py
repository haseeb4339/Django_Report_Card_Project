from django.shortcuts import render
from .models import Student

def get_students(request):
    queryset = Student.objects.all()

    return render(request, 'report/student.html', {'queryset': queryset})