# Generated by Django 4.0.3 on 2022-05-20 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vendor_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
