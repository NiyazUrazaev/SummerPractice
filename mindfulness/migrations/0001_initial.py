# Generated by Django 2.2.3 on 2020-05-10 15:25

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MindfulnessDiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Дневник с осознанностью',
                'verbose_name_plural': 'Дневники с осознанностью',
            },
        ),
        migrations.CreateModel(
            name='MindfulnessDiaryDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2020, 5, 10, 18, 25, 6, 261523))),
                ('work_info', models.CharField(default='', max_length=5000)),
                ('is_complete', models.BooleanField(default=False)),
                ('liked_things', models.TextField(default='')),
                ('disliked_things', models.TextField(default='')),
                ('day_evaluation', models.IntegerField(blank=True, choices=[(1, 'Понравилось'), (2, 'Не понравилось'), (3, 'Нейтрально')], null=True, verbose_name='Day evaluation')),
            ],
            options={
                'verbose_name': 'День в дневнике с осознанностью',
                'verbose_name_plural': 'Дни в дневнике с осознанностью',
            },
        ),
        migrations.CreateModel(
            name='MindfulnessPractice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_type', models.CharField(choices=[('Учебная', 'Учебная'), ('Производственная', 'Производственная')], max_length=30, verbose_name='Тип практики')),
                ('practice_addres', models.CharField(default='', max_length=500)),
                ('date_start', models.DateField(default=datetime.datetime(2020, 5, 10, 18, 25, 6, 323455))),
                ('date_end', models.DateField(default=datetime.datetime(2020, 5, 10, 18, 25, 6, 323487))),
            ],
            options={
                'verbose_name': 'Практика с осознанностью',
                'verbose_name_plural': 'Практики с осознанностью',
            },
        ),
        migrations.CreateModel(
            name='MindfulnessStudent',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('patronymic', models.CharField(default='', max_length=100, verbose_name='Отчество')),
                ('group', models.CharField(default='', max_length=10, verbose_name='Учебная группа')),
            ],
            options={
                'verbose_name': 'Студент с осознанностью',
                'verbose_name_plural': 'Студенты с осознанностью',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MindfulnessStudentPractice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(default='', verbose_name='Отзыв о практике')),
                ('aim', models.TextField(default='', verbose_name='Цель на практику')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindfulness.MindfulnessPractice', verbose_name='Практика')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindfulness.MindfulnessStudent', verbose_name='Студент')),
            ],
        ),
        migrations.AddField(
            model_name='mindfulnessstudent',
            name='practices',
            field=models.ManyToManyField(blank=True, null=True, through='mindfulness.MindfulnessStudentPractice', to='mindfulness.MindfulnessPractice', verbose_name='Наборы практик'),
        ),
    ]
