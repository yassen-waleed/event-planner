# Generated by Django 4.1.dev20220407055456 on 2022-06-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0002_rename_availability_date_availability_date_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability_date',
            name='end_date',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='availability_date',
            name='start_time',
            field=models.TimeField(),
        ),
    ]