# Generated by Django 5.0.4 on 2024-04-16 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], default=1),
            preserve_default=False,
        ),
    ]
