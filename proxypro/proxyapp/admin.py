
from django.contrib import admin
from.models import Student,Studentproxy
class Adminstudent(admin.ModelAdmin):
    list_display = ['sno','sname','location']
class Adminstudentproxy(admin.ModelAdmin):
    list_display = ['cno','cname','fee']
admin.site.register(Student,Adminstudent)
admin.site.register(Studentproxy,Adminstudentproxy)

