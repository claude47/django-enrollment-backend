from django.db import models
from django.forms import ModelForm
import uuid

GENDER_CHOICES = {
    "male": "male",
    "female": "female",
    "others": "others",
}

class Student(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    student_id = models.IntegerField(unique=True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_students'