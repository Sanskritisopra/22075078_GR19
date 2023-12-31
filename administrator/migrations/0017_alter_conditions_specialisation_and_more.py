# Generated by Django 4.2.6 on 2023-11-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0016_alter_doctors_detail_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conditions",
            name="specialisation",
            field=models.CharField(
                default=None, max_length=50, verbose_name="Specialization"
            ),
        ),
        migrations.AlterField(
            model_name="conditions",
            name="symptoms",
            field=models.CharField(
                default=None, max_length=50, primary_key=True, serialize=False
            ),
        ),
    ]
