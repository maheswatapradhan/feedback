from django.db import models
class Emp(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    salary=models.IntegerField()
    def __str__(self):
        return self.ename
