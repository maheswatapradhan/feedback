from django.db import models

class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    marks=models.IntegerField()
class studentproxy(Student):
    class Meta:
        proxy=True