# Generated by Django 5.0.4 on 2024-04-20 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptoalert',
            name='user',
        ),
    ]
