# Generated by Django 3.2.5 on 2021-07-19 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("torque", "0014_tableofcontentscache_rendered_html"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tableofcontentscache",
            name="rendered_data",
        ),
    ]
