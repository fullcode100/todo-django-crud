# Generated by Django 4.2.1 on 2023-06-02 03:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo', '0002_rename_member_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='firstname',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='lastname',
            new_name='todo',
        ),
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='todo',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
