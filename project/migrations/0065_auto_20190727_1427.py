# Generated by Django 2.0.13 on 2019-07-27 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0064_merge_20190727_1427'),
    ]

    operations = [
        migrations.DeleteModel(
            name='project1',
        ),
        migrations.AlterField(
            model_name='pro_stat',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='protags',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='userpro',
            name='project',
            field=models.ManyToManyField(to='project.Project'),
        ),
    ]
