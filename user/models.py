# -*- coding: utf-8 -*-

from django.db import models

from practice.models import Practice


class BaseUser(models.Model):

    name = models.CharField(
        max_length=100,
        default='',
    )

    second_name = models.CharField(
        max_length=100,
        default='',
    )

    patronymic = models.CharField(
        max_length=100,
        default='',
    )

    def full_name(self):
        return f"{self.second_name} {self.name} {self.patronymic}"

    def short_name(self):
        return f"{self.second_name} {self.name[0]}.{self.patronymic[0]}"

    class Meta:
        abstract = True


class Student(BaseUser):

    group = models.CharField(
        max_length=10,
        default='',
    )

    practices = models.ManyToManyField(
        Practice,
        null=True,
        blank=True,
    )


class Teacher(BaseUser):

    position = models.CharField(
        max_length=200,
        default='',
    )

