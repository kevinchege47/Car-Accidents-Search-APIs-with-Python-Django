# Generated by Django 4.1.2 on 2022-10-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='insurancecompany',
        ),
        migrations.RemoveField(
            model_name='insurancecompany',
            name='accidentlevel',
        ),
        migrations.RemoveField(
            model_name='insurancecompany',
            name='description',
        ),
        migrations.AlterField(
            model_name='cars',
            name='driverphone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='numberplate',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='insurancecompany',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
