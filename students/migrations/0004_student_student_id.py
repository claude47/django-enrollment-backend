# Generated by Django 5.0.4 on 2024-04-15 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_student_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=201, unique=True),
            preserve_default=False,
        ),
    ]
