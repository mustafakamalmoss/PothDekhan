# Generated by Django 3.1.1 on 2020-09-23 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Incidences',
            new_name='Places',
        ),
        migrations.AlterModelOptions(
            name='places',
            options={'verbose_name_plural': 'Places'},
        ),
    ]