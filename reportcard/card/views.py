from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator
from django.db.models import Q



def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')

        queryset = queryset.filter(Q(student_name__icontains = search)|
                                   Q(department__department__icontains=search)|
                                   Q(student_id__stud_id__icontains=search)|
                                   Q(student_email__icontains=search))

    paginator = Paginator(queryset, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'report/student.html', {'queryset': page_obj})




