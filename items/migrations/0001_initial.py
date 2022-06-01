# Generated by Django 4.0.3 on 2022-05-20 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenities_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='availability_date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='availability_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='customer_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='images2items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=300)),
                ('phone', models.TextField()),
                ('link', models.CharField(max_length=600)),
                ('about', models.CharField(max_length=1000)),
                ('price', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'good'), (4, 'very good'), (5, 'Excellent')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='items_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.type')),
            ],
        ),
        migrations.CreateModel(
            name='items_amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.amenities')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.rate'),
        ),
    ]