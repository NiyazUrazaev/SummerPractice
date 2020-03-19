import datetime

from django.db import models


class DiaryDay(models.Model):

    LIKE = 1
    DISLIKE = 2
    NEUTRAL = 3

    EVALUATION = (
        (LIKE, 'Понравилось'),
        (DISLIKE, 'Не понравилось'),
        (NEUTRAL, 'Нейтрально'),
    )

    date = models.DateField(
        default=datetime.datetime.today(),
    )

    work_info = models.CharField(
        max_length=5000,
        default='',
    )

    is_complete = models.BooleanField(
        default=False,
    )

    liked_things = models.TextField(
        default='',
    )

    disliked_things = models.TextField(
        default='',
    )

    day_evaluation = models.IntegerField(
        choices=EVALUATION,
        verbose_name='Day evaluation',
        null=True,
        blank=True,
    )


class Diary(models.Model):

    diary_days = models.ManyToManyField(
        DiaryDay
    )


class Practice(models.Model):

    STUDY = 'Учебная'
    WORK = 'Производственная'

    TYPE = (
        (STUDY, 'Учебная'),
        (WORK, 'Производственная'),
    )

    teacher = models.ForeignKey(
        'user.Teacher',
        on_delete=models.CASCADE,
        null=True,
    )

    practice_type = models.CharField(
        max_length=30,
        choices=TYPE,
        verbose_name='Type'
    )

    practice_addres = models.CharField(
        max_length=500,
        default='',
    )

    date_start=models.DateField(
        default=datetime.datetime.today(),
    )

    date_end=models.DateField(
        default=datetime.datetime.today(),
    )

    diary = models.ForeignKey(
        Diary,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
