# Generated by Django 4.2 on 2024-12-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollutionapp', '0006_remove_waterdata_coordinates_remove_waterdata_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waterdata',
            old_name='algea',
            new_name='water_colour',
        ),
        migrations.RemoveField(
            model_name='waterdata',
            name='aquatic',
        ),
        migrations.RemoveField(
            model_name='waterdata',
            name='odor',
        ),
        migrations.RemoveField(
            model_name='waterdata',
            name='pollutionform',
        ),
        migrations.RemoveField(
            model_name='waterdata',
            name='watercolour',
        ),
        migrations.AddField(
            model_name='waterdata',
            name='algae_blooms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='waterdata',
            name='aquatic_life',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='waterdata',
            name='latitude',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waterdata',
            name='longitude',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waterdata',
            name='odor_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='waterdata',
            name='pollution_evidence',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waterdata',
            name='nitrates',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='waterdata',
            name='oxygen',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='waterdata',
            name='ph',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='waterdata',
            name='phosphates',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='waterdata',
            name='turbidity',
            field=models.FloatField(),
        ),
    ]
