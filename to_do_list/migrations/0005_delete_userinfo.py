# Generated by Django 5.0.1 on 2024-04-09 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0004_userinfo_task_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userInfo',
        ),
    ]
