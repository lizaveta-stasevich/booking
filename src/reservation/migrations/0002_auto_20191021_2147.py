# Generated by Django 2.2.6 on 2019-10-21 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name_plural': 'cities'},
        ),
    ]
