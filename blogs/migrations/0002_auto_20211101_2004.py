# Generated by Django 3.2.7 on 2021-11-01 14:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdata',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blogdata',
            name='date',
        ),
        migrations.AddField(
            model_name='blogdata',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 20, 4, 36, 664959)),
        ),
        migrations.AddField(
            model_name='blogdata',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
