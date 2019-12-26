# Generated by Django 2.2.3 on 2019-12-26 21:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_auto_20191227_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryday',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='diaryday',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 12, 27, 0, 4, 19, 100678)),
        ),
        migrations.AlterField(
            model_name='practice',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2019, 12, 27, 0, 4, 19, 129247)),
        ),
        migrations.AlterField(
            model_name='practice',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2019, 12, 27, 0, 4, 19, 129224)),
        ),
        migrations.AlterField(
            model_name='practice',
            name='diary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='practice.Diary'),
        ),
    ]
