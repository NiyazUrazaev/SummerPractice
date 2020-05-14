# -*- coding: utf-8 -*-

import pandas as pd
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response

from gamification.models import (
    GamificationPractice, GamificationDiary,
    GamificationStudent, GamificationDiaryDay, GamificationStudentPractice,
)
from practice.abstract_views import (
    AbstractPracticeAllView, AbstractDiaryDaysView,
    AbstractPracticeView, AbstractPrintDiaryView,
    AbstractDayView, AbstractPracticeReviewView,
)


class GamificationPracticeAllView(AbstractPracticeAllView):
    """Вывод списка всех практик с геймификацией"""
    Model = GamificationPractice


class GamificationPracticeView(AbstractPracticeView):
    """Получалка инфы о практике с геймификацией"""
    Model = GamificationPractice


class GamificationGetAllDiaryDaysView(AbstractDiaryDaysView):
    """Ручка для получения всех дней в дневнике с геймификацией"""
    Model = GamificationDiary


class GamificationPrintDiaryView(AbstractPrintDiaryView):
    """Ручка для печати дневника с геймификацией"""
    Model = GamificationDiary
    StudentModel = GamificationStudent


class GamificationCreateDiaryView(APIView):
    """Создание нового дневника с геймификацией"""

    def post(self, request):

        practice_id = request.POST.get('practice', None)
        if practice_id is None:
            return Response(status=400, data='No practice in kwargs!')

        practice = GamificationPractice.objects.get(id=practice_id)

        if GamificationDiary.objects.filter(practice=practice).exists():
            return Response(status=400, data='You have created diary yet!')

        daterange = pd.date_range(practice.date_start, practice.date_end)
        diary = GamificationDiary.objects.create()
        days = []
        for day in daterange:
            dday = GamificationDiaryDay.objects.create(
                date=day,
                work_info='',
            )
            diary.diary_days.add(dday)

            days.append(model_to_dict(dday))

        diary.practice = practice
        diary.save()
        practice.save()
        return Response(status=200, data={'diary_id': diary.id, 'days': days})


class GamificationGetDayView(AbstractDayView):
    """Получаем инфу об конкретном дне с геймификацией"""
    Model = GamificationDiaryDay


class GamificationEditDayView(APIView):
    """Создаем/редактируем инфу об конкретном дне с геймификацией"""

    def post(self, request):

        day_id = request.POST.get('day', None)
        work_info = request.POST.get('work_info', '')
        liked_things = request.POST.get('liked_things', '')
        disliked_things = request.POST.get('disliked_things', '')
        day_evaluation = request.POST.get('day_evaluation', None)

        if day_id is not None:

            # TODO: Сделать покрасивее
            day = GamificationDiaryDay.objects.get(id=day_id)
            day.work_info = work_info
            if work_info != '':
                day.is_complete = True
            day.liked_things = liked_things
            day.disliked_things = disliked_things
            day.day_evaluation = day_evaluation
            day.save()

            return Response(
                status=200,
                data=model_to_dict(day)
            )
        else:
            return Response(status=400, data='No day in kwargs!')


class GamificationPracticeReviewView(AbstractPracticeReviewView):
    """Ручка для получения всех отзывов о практики с геймификацией"""

    Model = GamificationStudentPractice
