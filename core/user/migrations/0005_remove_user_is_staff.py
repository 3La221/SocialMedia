# Generated by Django 5.0.1 on 2024-01-28 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0004_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
