# Generated by Django 2.2.2 on 2019-07-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('groups', '0010_auto_20190702_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progroup',
            name='project',
            field=models.ManyToManyField(to='project.Project'),
        ),
    ]