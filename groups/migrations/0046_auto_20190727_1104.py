# Generated by Django 2.0.13 on 2019-07-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0045_auto_20190727_1100'),
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
