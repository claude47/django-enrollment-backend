from django.db import models

class Student(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)