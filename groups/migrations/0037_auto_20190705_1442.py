# Generated by Django 2.2.2 on 2019-07-05 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0036_auto_20190705_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='project',
            field=models.ManyToManyField(blank=True, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(blank=True, default=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User', to=settings.AUTH_USER_MODEL), to=settings.AUTH_USER_MODEL),
        ),
    ]
