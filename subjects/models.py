from django.db import models

class Subject(models.Model):
    code = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)