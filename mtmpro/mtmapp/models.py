from django.db import models

class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    marks=models.IntegerField()
    def __str__(self):
        return self.sname
class Course(models.Model):
    student=models.ManyToManyField(Student)
    cno=models.IntegerField()
    cname=models.CharField(max_length=100)
    fee=models.IntegerField()
    def __str__(self):
        return self.cname

