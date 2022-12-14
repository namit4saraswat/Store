# Generated by Django 4.1.2 on 2022-10-22 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_state_created_on_state_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='state',
            name='status',
            field=models.BooleanField(blank=True, default=1, editable=False),
        ),
    ]
