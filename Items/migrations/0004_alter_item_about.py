# Generated by Django 4.1.dev20220407055456 on 2022-06-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0003_alter_availability_date_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='about',
            field=models.TextField(),
        ),
    ]
