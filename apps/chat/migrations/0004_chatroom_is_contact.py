# Generated by Django 4.1.5 on 2023-01-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_message_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='is_contact',
            field=models.BooleanField(default=False),
        ),
    ]