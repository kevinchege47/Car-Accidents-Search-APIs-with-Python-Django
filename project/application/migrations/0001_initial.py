# Generated by Django 4.1.2 on 2022-10-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('degreeseverity', models.CharField(choices=[('Fatal Injury Crash', 'Fatal Injury Crash'), ('Major Injury Crash', 'Major Injury Crash'), ('Minor Injury Crash', 'Minor Injury Crash'), ('Minimal Injury Crash', 'Minimal Injury Crash')], max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('head_office_location', models.CharField(max_length=50, null=True)),
                ('phone', models.IntegerField(max_length=15, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('accidentlevel', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberplate', models.CharField(max_length=50, null=True)),
                ('makemodel', models.CharField(max_length=50, null=True)),
                ('driverphone', models.IntegerField(max_length=15, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('accidents', models.ManyToManyField(blank=True, to='application.accidents')),
                ('insurancecompany', models.ManyToManyField(blank=True, to='application.insurancecompany')),
            ],
        ),
    ]