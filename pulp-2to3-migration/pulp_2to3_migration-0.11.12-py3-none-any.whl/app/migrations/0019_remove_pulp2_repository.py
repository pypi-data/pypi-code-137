# Generated by Django 2.2.16 on 2020-11-12 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulp_2to3_migration', '0018_pulp2distributor_pulp2_repos'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pulp2distributor',
            unique_together={('pulp2_object_id',)},
        ),
        migrations.RemoveField(
            model_name='pulp2distributor',
            name='pulp2_repository',
        ),
    ]
