# Generated by Django 4.2.3 on 2023-08-13 22:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_profile_matches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='matches',
            field=models.CharField(default='<django.db.models.fields.IntegerField>', max_length=256, validators=[django.core.validators.int_list_validator]),
        ),
    ]
