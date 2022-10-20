# Generated by Django 3.2.7 on 2021-09-05 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("torque", "0024_auto_20210905_1535"),
    ]

    operations = [
        migrations.AlterField(
            model_name="field",
            name="sheet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fields",
                to="torque.spreadsheet",
            ),
        ),
        migrations.AlterField(
            model_name="field",
            name="sheet_config",
            field=models.ManyToManyField(
                related_name="valid_fields", to="torque.SheetConfig"
            ),
        ),
    ]
