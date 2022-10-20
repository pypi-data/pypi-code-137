# Generated by Django 3.2.7 on 2022-02-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("torque", "0032_searchcachedocument_filtered_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="CsvSpecification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fields", models.JSONField()),
                ("name", models.TextField()),
                ("filename", models.TextField()),
                ("documents", models.ManyToManyField(to="torque.Document")),
            ],
        ),
    ]
