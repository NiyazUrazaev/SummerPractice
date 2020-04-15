# -*- coding: utf-8 -*-

from django.db import models

from practice.models import Practice
from django.contrib.auth.models import User


class BaseUser(User):

    patronymic = models.CharField(
        max_length=100,
        default='',
        verbose_name='Отчество',
    )

    def full_name(self):
        return "{0} {1} {2}".format(
            self.last_name, self.first_name, self.patronymic)

    def short_name(self):
        return "{0} {1}.{2}".format(
            self.last_name, self.first_name[0], self.patronymic[0])

    class Meta:
        abstract = True


class Student(BaseUser):

    group = models.CharField(
        max_length=10,
        default='',
        verbose_name='Учебная группа',
    )

    practices = models.ManyToManyField(
        Practice,
        null=True,
        blank=True,
        verbose_name='Наборы практик',
    )


class Teacher(BaseUser):

    position = models.CharField(
        max_length=200,
        default='',
    )

