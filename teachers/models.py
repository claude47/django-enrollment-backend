from django.db import models
import uuid

class Teacher(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    teacher_id = models.IntegerField(unique=True)
    teacher_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'tbl_teachers'