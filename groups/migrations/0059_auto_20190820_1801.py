# Generated by Django 2.2.3 on 2019-08-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('groups', '0058_auto_20190814_2305'),
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
