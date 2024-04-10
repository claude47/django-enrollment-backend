from django.db import models
from students.models import Student
from subjects.models import Subject

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - Enrolled on {self.enrollment_date}"