# Generated by Django 2.2.6 on 2019-11-04 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'cities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('passport_series', models.CharField(max_length=2)),
                ('passport_number', models.CharField(max_length=6, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name_plural': 'passengers',
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(unique=True)),
                ('dep_time', models.TimeField()),
                ('arr_time', models.TimeField()),
                ('place_type', models.CharField(blank=True, choices=[('ОБЩ', 'Общий'), ('ПЛЦ', 'Плацкартный'), ('КУП', 'Купейный'), (None, '---')], default='', max_length=3)),
                ('arr_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='reservation.City')),
                ('dep_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='reservation.City')),
            ],
            options={
                'verbose_name_plural': 'trains',
                'ordering': ['dep_station'],
            },
        ),
    ]