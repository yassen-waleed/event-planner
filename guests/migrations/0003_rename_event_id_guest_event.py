# Generated by Django 4.0.3 on 2022-06-16 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_rename_event_guest_event_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='event_id',
            new_name='event',
        ),
    ]
