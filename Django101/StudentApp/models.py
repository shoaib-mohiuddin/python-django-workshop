from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    age=models.IntegerField()
    loc=models.CharField(max_length=20,null=True)