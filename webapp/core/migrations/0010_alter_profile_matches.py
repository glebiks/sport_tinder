# Generated by Django 4.2.3 on 2023-08-14 00:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_profile_matches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='matches',
            field=models.CharField(default='0', max_length=256, validators=[django.core.validators.int_list_validator]),
        ),
    ]
