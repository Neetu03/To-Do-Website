# Generated by Django 5.0.1 on 2024-01-31 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='Task',
        ),
    ]