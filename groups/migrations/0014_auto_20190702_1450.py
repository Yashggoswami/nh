# Generated by Django 2.2.2 on 2019-07-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('groups', '0013_auto_20190702_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progroup',
            name='project',
            field=models.ManyToManyField(to='project.Project'),
        ),
    ]
