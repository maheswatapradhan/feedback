from django.db import models
class Customer(models.Model):
    cname=models.CharField(max_length=100)
    sales=models.IntegerField()
class Student(Customer):
    sname=models.CharField(max_length=100)
    marks=models.IntegerField()
class Emp(Student):
    ename=models.CharField(max_length=100)
    salary=models.IntegerField()


