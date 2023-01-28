# Generated by Django 4.1.5 on 2023-01-28 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_skills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('employment_type', models.CharField(choices=[('full employment', 'full employment'), ('part-time employment', 'part-time employment'), ('entrepreneur', 'entrepreneur'), ('freelance', 'freelance'), ('contract', 'contract'), ('internship', 'internship'), ('vocational training', 'vocational training'), ('Seasonal', 'Seasonal')], max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=255)),
                ('job_type', models.CharField(choices=[('office work', 'office work'), ('hybrid workflow', 'hybrid workflow'), ('remote work', 'remote work')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_position', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EducationInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educational_institution', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=200)),
                ('specialization', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('average_score', models.PositiveIntegerField()),
                ('activities_communities', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_education', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
