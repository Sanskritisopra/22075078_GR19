# Generated by Django 4.2.6 on 2023-10-30 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0003_delete_customuser"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="patient",
            table="Patient",
        ),
    ]
