# Generated by Django 4.0.4 on 2022-05-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_alter_review_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-time_created']},
        ),
        migrations.AddField(
            model_name='ticket',
            name='time_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
