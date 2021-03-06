# Generated by Django 3.2.9 on 2022-03-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferenceroom', '0002_auto_20220302_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomnumber', models.CharField(max_length=50, unique=True)),
                ('roomtype', models.CharField(max_length=50)),
                ('dateofuse', models.CharField(max_length=50)),
                ('timeuse', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('emailadd', models.CharField(max_length=50)),
                ('contactNum', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
