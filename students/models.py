from django.db import models
class Student(models.Model):
    name =models.CharField(max_length=27)
    Level=models.CharField(max_length=27)
    fee  =models.FloatField(max_length=7, default='500')
    about=models.TextField(blank=True, null=True)
# Create your models here.
