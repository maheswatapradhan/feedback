from django.db import models
from multiselectfield import MultiSelectField
class EnquaryData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    COURSES_CHOICES=(
        ('PY','Python'),
        ('DJ','Django'),
        ('RA','Rest API'),
        ('UI','User Interface')
    )
    course=MultiSelectField(choices=COURSES_CHOICES,max_length=100)
    LOCATION_CHOICES=(
        ('HYD','Hyderbad'),
        ('BANG','Bangalore'),
        ('che','Chennai')
    )
    location=MultiSelectField(choices=LOCATION_CHOICES,max_length=100)
    gender=models.CharField(max_length=100)
    start_date=models.DateField(max_length=100)

