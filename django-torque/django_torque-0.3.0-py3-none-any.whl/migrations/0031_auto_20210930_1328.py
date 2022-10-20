# Generated by Django 3.2.7 on 2021-09-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("torque", "0030_auto_20210927_1304"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="document",
            name="unique_key",
        ),
        migrations.AddField(
            model_name="field",
            name="attached",
            field=models.BooleanField(default=True),
        ),
        migrations.AddConstraint(
            model_name="document",
            constraint=models.UniqueConstraint(
                fields=("collection", "key"), name="unique_key"
            ),
        ),
    ]
