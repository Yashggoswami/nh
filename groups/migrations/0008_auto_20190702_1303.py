# Generated by Django 2.2.2 on 2019-07-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('groups', '0007_auto_20190701_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progroup',
            name='project',
            field=models.ManyToManyField(to='project.Project'),
        ),
    ]
