from django.db import models

# Create your models here.
from practice.models import BaseAppsDiaryDay, BasePractice
from user.models import BaseStudent


class GamificationPractice(BasePractice):
    """Практика с gamification"""

    class Meta:
        verbose_name = "Практика с gamification"
        verbose_name_plural = "Практики с gamification"


class GamificationDiaryDay(BaseAppsDiaryDay):
    """День в дневнике с gamification"""

    class Meta:
        verbose_name = "День в дневнике с gamification"
        verbose_name_plural = "Дни в дневнике с gamification"


class GamificationDiary(models.Model):
    """Дневник с gamification"""

    diary_days = models.ManyToManyField(
        GamificationDiaryDay
    )

    practice = models.ForeignKey(
        GamificationPractice,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Дневник с gamification"
        verbose_name_plural = "Дневники с gamificationn"


class GamificationStudent(BaseStudent):
    """Студент с геймификацией"""

    practices = models.ManyToManyField(
        GamificationPractice,
        null=True,
        blank=True,
        verbose_name='Наборы практик',
        through='GamificationStudentPractice',
    )

    class Meta:
        verbose_name = "Студент с геймификацией"
        verbose_name_plural = "Студенты с геймификацией"


class GamificationStudentPractice(models.Model):
    """Связующая для геймификации"""

    student = models.ForeignKey(
        GamificationStudent,
        on_delete=models.CASCADE,
        verbose_name='Студент',
    )

    practice = models.ForeignKey(
        GamificationPractice,
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