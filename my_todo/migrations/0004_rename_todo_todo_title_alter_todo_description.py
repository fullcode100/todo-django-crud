# Generated by Django 4.2.1 on 2023-06-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo', '0003_rename_firstname_todo_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(),
        ),
    ]
