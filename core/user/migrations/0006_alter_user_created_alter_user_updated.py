# Generated by Django 5.0.1 on 2024-01-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0005_remove_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
