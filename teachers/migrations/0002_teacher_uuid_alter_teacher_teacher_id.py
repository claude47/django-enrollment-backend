# Generated by Django 5.0.4 on 2024-04-18 07:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_id',
            field=models.IntegerField(unique=True),
        ),
    ]
