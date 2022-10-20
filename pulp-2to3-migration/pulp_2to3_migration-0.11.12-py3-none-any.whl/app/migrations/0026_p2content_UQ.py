# Generated by Django 2.2.19 on 2021-03-09 01:47

from django.db import migrations, models
from django.db.models import Count, F


class Migration(migrations.Migration):

    dependencies = [
        ('pulp_2to3_migration', '0025_remove_p2content_dups'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pulp2content',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='pulp2content',
            constraint=models.UniqueConstraint(fields=('pulp2_id', 'pulp2_content_type_id', 'pulp2_repo', 'pulp2_subid'), name='unique_with_optional'),
        ),
        migrations.AddConstraint(
            model_name='pulp2content',
            constraint=models.UniqueConstraint(condition=models.Q(pulp2_repo=None), fields=('pulp2_id', 'pulp2_content_type_id', 'pulp2_subid'), name='unique_without_optional'),
        ),
    ]
