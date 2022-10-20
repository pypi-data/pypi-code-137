# Generated by Django 3.1.7 on 2021-03-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("torque", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="template",
            constraint=models.UniqueConstraint(
                fields=("sheet", "type", "name"), name="unique_template"
            ),
        ),
    ]
