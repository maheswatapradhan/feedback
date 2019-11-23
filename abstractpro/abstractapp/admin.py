from django.contrib import admin
from .models import Customer,Student,Emp
class Adminstudent(admin.ModelAdmin):
    list_display = ['name','location','marks']
class Admincustomer(admin.ModelAdmin):
    list_display = ['name','location','sales']
class Adminemp(admin.ModelAdmin):
    list_display = ['name','location','salary']
admin.site.register(Student,Adminstudent)
admin.site.register(Customer,Admincustomer)
admin.site.register(Emp,Adminemp)

