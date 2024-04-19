from django.db import models
import uuid

class Subject(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    code = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'tbl_subjects'