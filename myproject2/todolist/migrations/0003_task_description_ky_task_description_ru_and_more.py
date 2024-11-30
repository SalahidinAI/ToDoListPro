# Generated by Django 5.1.3 on 2024-11-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_name_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
