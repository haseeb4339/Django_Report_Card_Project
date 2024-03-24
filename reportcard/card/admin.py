from django.contrib import admin

from .models import Student, StudentID, Subject, SubjectMarks, Department

admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(SubjectMarks, SubjectMarksAdmin)
admin.site.register(Department)
