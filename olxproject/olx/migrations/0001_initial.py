# Generated by Django 4.2.5 on 2023-09-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=20)),
                ('km', models.CharField(max_length=20)),
                ('vehiclemodel', models.CharField(max_length=4)),
            ],
        ),
    ]
