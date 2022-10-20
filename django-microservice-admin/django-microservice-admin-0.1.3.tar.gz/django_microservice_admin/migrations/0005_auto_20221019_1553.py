# Generated by Django 3.2.7 on 2022-10-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_microservice_admin', '0004_alter_adminapps_redirect_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminapps',
            old_name='app_name',
            new_name='project_name',
        ),
        migrations.AddField(
            model_name='adminapps',
            name='tab_name',
            field=models.CharField(max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
