# Generated by Django 2.2.3 on 2019-07-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('groups', '0045_auto_20190726_1453'),
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
