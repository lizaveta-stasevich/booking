# Generated by Django 2.2.6 on 2019-10-26 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20191021_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(unique=True)),
                ('dep_time', models.TimeField()),
                ('arr_time', models.TimeField()),
                ('carriage_type', models.CharField(max_length=20)),
                ('arr_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='reservation.City')),
                ('dep_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='reservation.City')),
            ],
            options={
                'verbose_name_plural': 'trains',
                'ordering': ['dep_station'],
            },
        ),
    ]
