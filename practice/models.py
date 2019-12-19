import datetime

from django.db import models


class DiaryDay(models.Model):

    date = models.DateField(
        default=datetime.datetime.today(),
    )

    work_info = models.CharField(
        max_length=5000,
        default='',
    )


class Diary(models.Model):

    diary_days = models.ManyToManyField(DiaryDay)


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

    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
