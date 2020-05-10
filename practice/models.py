import datetime

from django.db import models


class BaseDiaryDay(models.Model):
    """Базовый класс для одного дня у всех аппов"""

    date = models.DateField(
        default=datetime.datetime.today(),
    )

    work_info = models.CharField(
        max_length=5000,
        default='',
    )

    class Meta:
        abstract = True


class BaseAppsDiaryDay(BaseDiaryDay):
    """
    Базовый класс для аппов gamification и mindfullness
    одного дня у дневника
    """

    LIKE = 1
    DISLIKE = 2
    NEUTRAL = 3

    EVALUATION = (
        (LIKE, 'Понравилось'),
        (DISLIKE, 'Не понравилось'),
        (NEUTRAL, 'Нейтрально'),
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

    class Meta:
        abstract = True


class BasePractice(models.Model):
    """Базовы класс для практик всех аппов"""

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
        verbose_name='Тип практики'
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

    class Meta:
        abstract = True


class ClassicPractice(BasePractice):
    """Практика без gamification и без mindfullness"""

    class Meta:
        verbose_name = "Практика без gamification и без mindfullness"
        verbose_name_plural = "Практики без gamification и без mindfullness"


class ClassicDiaryDay(BaseDiaryDay):
    """День практики в дневнике без gamification и без mindfullness"""

    class Meta:
        verbose_name = (
            "День практики в дневнике без gamification и без mindfullness"
        )
        verbose_name_plural = (
            "Дни практики в дневнике без gamification и без mindfullness"
        )


class ClassicDiary(models.Model):
    """Дневник без gamification и без mindfullness"""
    diary_days = models.ManyToManyField(
        ClassicDiaryDay
    )

    practice = models.ForeignKey(
        ClassicPractice,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Дневник без gamification и без mindfullness"
        verbose_name_plural = "Дневники без gamification и без mindfullness"
