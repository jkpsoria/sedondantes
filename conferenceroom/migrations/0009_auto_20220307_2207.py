# Generated by Django 3.2.9 on 2022-03-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferenceroom', '0008_auto_20220307_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='contactNum',
        ),
        migrations.RemoveField(
            model_name='room',
            name='emailadd',
        ),
        migrations.AddField(
            model_name='user',
            name='contactNum',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
