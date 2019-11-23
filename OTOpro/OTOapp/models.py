from django.db import models

class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.sname
class Course(models.Model):
    abc=models.OneToOneField(Student)
    cno=models.IntegerField()
    cname=models.CharField(max_length=100)
    fee=models.IntegerField()
    def __str__(self):
        return self.cname

