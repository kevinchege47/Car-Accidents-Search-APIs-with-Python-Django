# Generated by Django 4.1.2 on 2022-10-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_remove_cars_insurancecompany_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='insurancecompany',
            field=models.ManyToManyField(to='application.insurancecompany'),
        ),
    ]