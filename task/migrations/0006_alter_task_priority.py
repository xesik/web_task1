# Generated by Django 4.1 on 2024-12-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Высокий', 'Высокий(1)'), ('Низкий', 'Низкий(3)'), ('Средний', 'Средний(2)')], max_length=7),
        ),
    ]
