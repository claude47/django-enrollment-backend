from django.db import models

class Enrollment(models.Model):
    student = models.ForeignKey(
        "students.Student", 
        on_delete=models.CASCADE
        )
    teacher = models.ForeignKey(
        "teachers.Teacher", 
        on_delete=models.CASCADE
        )
    subject = models.ManyToManyField(
        "subjects.Subject"
        ) 
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - Enrolled on {self.enrollment_date}"