# Generated by Django 2.0.13 on 2019-07-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0041_merge_20190713_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='project',
            field=models.ManyToManyField(blank=True, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='groupprojects',
            name='project',
            field=models.ManyToManyField(to='project.Project'),
        ),
    ]
