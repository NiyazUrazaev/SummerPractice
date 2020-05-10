from django.db import models

# Create your models here.
from practice.models import BaseAppsDiaryDay, BasePractice
from user.models import BaseStudent


class MindfulnessPractice(BasePractice):
    """Практика с осознанностью"""

    class Meta:
        verbose_name = "Практика с осознанностью"
        verbose_name_plural = "Практики с осознанностью"


class MindfulnessDiaryDay(BaseAppsDiaryDay):
    """День в дневнике с осознанностью"""

    class Meta:
        verbose_name = "День в дневнике с осознанностью"
        verbose_name_plural = "Дни в дневнике с осознанностью"


class MindfulnessDiary(models.Model):
    """Дневник с осознанностью"""

    diary_days = models.ManyToManyField(
        MindfulnessDiaryDay
    )

    practice = models.ForeignKey(
        MindfulnessPractice,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Дневник с осознанностью"
        verbose_name_plural = "Дневники с осознанностью"


class MindfulnessStudent(BaseStudent):
    """Студент с осознанностью"""

    practices = models.ManyToManyField(
        MindfulnessPractice,
        null=True,
        blank=True,
        verbose_name='Наборы практик',
        through='MindfulnessStudentPractice',
    )

    class Meta:
        verbose_name = "Студент с осознанностью"
        verbose_name_plural = "Студенты с осознанностью"


class MindfulnessStudentPractice(models.Model):
    """Связующая для осознанности"""

    student = models.ForeignKey(
        MindfulnessStudent,
        on_delete=models.CASCADE,
        verbose_name='Студент',
    )

    practice = models.ForeignKey(
        MindfulnessPractice,
        on_delete=models.CASCADE,
        verbose_name='Практика',
    )

    review = models.TextField(
        default='',
        verbose_name='Отзыв о практике',
    )

    aim = models.TextField(
        default='',
        verbose_name='Цель на практику',
    )