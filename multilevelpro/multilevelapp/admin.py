from django.contrib import admin
from .models import Student,Customer,Emp
class Adminstudent(admin.ModelAdmin):
    list_display = ['sname','marks']
class Admincustomer(admin.ModelAdmin):
    list_display = ['cname','sales']
class Adminemp(admin.ModelAdmin):
    list_display = ['ename','salary']
admin.site.register(Student,Adminstudent)
admin.site.register(Customer,Admincustomer)
admin.site.register(Emp,Adminemp)
