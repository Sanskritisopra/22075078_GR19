# Generated by Django 4.2.6 on 2023-10-31 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0007_rename_appoint_id_bill_appoint"),
    ]

    operations = [
        migrations.RenameField(
            model_name="labreport",
            old_name="appoint_id",
            new_name="appoint",
        ),
    ]
