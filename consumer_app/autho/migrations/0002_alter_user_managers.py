# Generated by Django 4.2.1 on 2023-05-31 16:29

import autho.managers
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("autho", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", autho.managers.UserManager()),
            ],
        ),
    ]
