# Generated by Django 4.0.3 on 2022-05-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=5000)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]