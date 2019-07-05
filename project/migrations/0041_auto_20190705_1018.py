# Generated by Django 2.2.2 on 2019-07-05 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0040_auto_20190704_1928'),
    ]

    operations = [
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