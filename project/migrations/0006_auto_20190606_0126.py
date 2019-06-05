# Generated by Django 2.2.1 on 2019-06-05 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20190606_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='userpro',
            name='current_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
    ]