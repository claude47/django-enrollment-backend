# Generated by Django 5.0.4 on 2024-04-19 00:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterModelTable(
            name='student',
            table='tbl_students',
        ),
    ]
