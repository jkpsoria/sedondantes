# Generated by Django 3.2.9 on 2022-03-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferenceroom', '0014_alter_room_dateofuse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='dateofuse',
            field=models.DateField(blank=True, default='', max_length=50, null=True),
        ),
    ]
