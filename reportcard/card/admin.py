from django.contrib import admin

from .models import Student, StudentID, Subject, SubjectMarks

admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Subject)
admin.site.register(SubjectMarks)
