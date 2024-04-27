# Generated by Django 5.0.4 on 2024-04-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_student_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='present',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
