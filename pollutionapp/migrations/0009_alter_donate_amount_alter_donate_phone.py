# Generated by Django 4.2 on 2024-12-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollutionapp', '0008_alter_waterdata_algae_blooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='amount',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='donate',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
