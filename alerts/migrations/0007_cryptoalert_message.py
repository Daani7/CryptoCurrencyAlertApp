# Generated by Django 5.0.4 on 2024-04-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0006_alter_cryptoalert_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptoalert',
            name='message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
