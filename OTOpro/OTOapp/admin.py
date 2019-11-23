from django.contrib import admin
from .models import Student,Course

class AdminStudent(admin.ModelAdmin):
    list_display =['sno','sname','location']
class AdminCourse(admin.ModelAdmin):
    list_display =['cno','cname','fee']

admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse )
