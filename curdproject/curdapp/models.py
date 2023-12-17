from django.db import models

# Create your models here.
class students(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile_no=models.BigIntegerField()
    Email=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    Cgpa=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
   
   

