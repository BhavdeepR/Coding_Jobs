# Generated by Django 3.1.1 on 2025-05-04 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='content',
        ),
        migrations.RemoveField(
            model_name='application',
            name='experience',
        ),
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.FileField(default='', upload_to='resumes/'),
            preserve_default=False,
        ),
    ]
