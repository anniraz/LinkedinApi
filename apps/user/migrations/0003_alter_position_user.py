# Generated by Django 4.1.5 on 2023-01-29 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_skills_position_educationinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_position', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]