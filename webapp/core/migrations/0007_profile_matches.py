# Generated by Django 4.2.3 on 2023-08-13 20:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_tg_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='matches',
            field=models.CharField(default='[]', max_length=256, validators=[django.core.validators.int_list_validator]),
        ),
    ]
