# Generated by Django 2.2.3 on 2019-08-06 11:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('resources', '0004_language_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='discription',
            new_name='description',
        ),
    ]
