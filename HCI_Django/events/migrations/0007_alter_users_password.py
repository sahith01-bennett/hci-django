# Generated by Django 4.1.7 on 2023-04-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_booking_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
