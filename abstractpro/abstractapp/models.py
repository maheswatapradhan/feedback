from django.db import models
class commandata(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    class Meta:
        abstract=True
class Emp(commandata):
    salary=models.IntegerField()
class Student(commandata):
    marks=models.IntegerField()
class Customer(commandata):
    sales=models.IntegerField()
