# Generated by Django 2.2.2 on 2019-07-04 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0038_auto_20190704_1922'),
        ('groups', '0022_auto_20190704_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, unique=True)),
                ('bio', models.TextField(max_length=250, null=True)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usrgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Groupdetails')),
                ('users', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Groupdetails')),
                ('project', models.ManyToManyField(to='project.Project')),
            ],
        ),
    ]
