from django.contrib import admin

from .models import Student, StudentID, Subject, SubjectMarks, Department

admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Subject)
admin.site.register(SubjectMarks)
admin.site.register(Department)
