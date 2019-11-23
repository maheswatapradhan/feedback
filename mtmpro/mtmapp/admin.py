from django.contrib import admin
from.models import Student,Course
class Adminstudent(admin.ModelAdmin):
    list_display = ['sno','sname','location']
class Admincrouse(admin.ModelAdmin):
    list_display = ['cno','cname','fee']
admin.site.register(Student,Adminstudent)
admin.site.register(Course,Admincrouse)
