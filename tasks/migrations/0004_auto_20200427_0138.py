# Generated by Django 3.0.5 on 2020-04-27 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200426_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_name',
            field=models.TextField(max_length=300),
        ),
    ]
