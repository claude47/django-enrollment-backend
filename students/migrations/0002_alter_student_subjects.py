# Generated by Django 5.0.4 on 2024-04-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('subjects', '0002_rename_subject_code_subject_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(null=True, related_name='students', to='subjects.subject'),
        ),
    ]
