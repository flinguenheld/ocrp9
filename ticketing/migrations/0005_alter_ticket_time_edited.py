# Generated by Django 4.0.4 on 2022-05-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0004_alter_ticket_time_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time_edited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
