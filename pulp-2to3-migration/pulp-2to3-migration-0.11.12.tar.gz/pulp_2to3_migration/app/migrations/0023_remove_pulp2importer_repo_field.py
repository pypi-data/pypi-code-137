# Generated by Django 2.2.17 on 2021-02-24 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulp_2to3_migration', '0022_add_structured_deb_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pulp2importer',
            name='pulp2_repository',
        ),
    ]
