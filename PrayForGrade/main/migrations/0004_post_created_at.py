# Generated by Django 4.0.5 on 2022-06-14 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 12, 23, 7, 568731)),
        ),
    ]
