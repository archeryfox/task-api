# Generated by Django 4.2.6 on 2024-05-08 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker_api', '0016_alter_team_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_tracker_api.user', verbose_name='Пользователь'),
        ),
    ]
