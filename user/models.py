# -*- coding: utf-8 -*-

from django.db import models

from practice.models import ClassicPractice
from django.contrib.auth.models import User


class BaseUser(User):
    """Базовый класс пользователя для всех аппов"""

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


class BaseStudent(BaseUser):
    """Базовый класс студента для всех аппов"""

    group = models.CharField(
        max_length=10,
        default='',
        verbose_name='Учебная группа',
    )

    class Meta:
        abstract = True


class Teacher(BaseUser):
    """Классический преподаватель"""
    position = models.CharField(
        max_length=200,
        default='',
    )

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class ClassicStudent(BaseStudent):
    """Студент без осознанности и геймификации"""

    practices = models.ManyToManyField(
        ClassicPractice,
        null=True,
        blank=True,
        verbose_name='Наборы практик',
    )

    class Meta:
        verbose_name = "Студент без осознанности и геймификации"
        verbose_name_plural = "Студенты без осознанности и геймификации"

