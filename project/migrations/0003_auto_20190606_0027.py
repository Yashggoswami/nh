# Generated by Django 2.2.1 on 2019-06-05 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20190606_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpro',
            name='current_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
    ]
