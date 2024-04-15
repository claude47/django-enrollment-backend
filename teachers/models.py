from django.db import models

class Teacher(models.Model):
    teacher_id = models.IntegerField(unique=True)
    teacher_name = models.CharField(max_length=100)
    