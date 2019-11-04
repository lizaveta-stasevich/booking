# Generated by Django 2.2.6 on 2019-10-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20191029_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='passport_number',
            field=models.CharField(max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='patronymic',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='phone',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='surname',
            field=models.CharField(max_length=30),
        ),
    ]
