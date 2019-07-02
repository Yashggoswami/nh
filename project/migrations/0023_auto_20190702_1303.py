# Generated by Django 2.2.2 on 2019-07-02 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('project', '0022_auto_20190701_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpro',
            name='completion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userpro',
            name='current_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='userprodetal',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
    ]
