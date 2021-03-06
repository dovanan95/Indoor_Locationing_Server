# Generated by Django 3.1.7 on 2021-03-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location_ID', models.CharField(max_length=250)),
                ('x_coordinate', models.FloatField(max_length=250)),
                ('y_coordinate', models.FloatField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSID', models.CharField(max_length=250)),
                ('RSSI', models.FloatField(max_length=250)),
                ('Time', models.DateTimeField()),
                ('BSSID', models.CharField(max_length=250)),
                ('Location_ID', models.CharField(max_length=250)),
            ],
        ),
    ]
