# -*- coding: utf-8 -*-

import pandas as pd
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response

from mindfulness.models import (
    MindfulnessPractice, MindfulnessDiary,
    MindfulnessStudent, MindfulnessDiaryDay,
    MindfulnessStudentPractice
)
from practice.abstract_views import (
    AbstractPracticeAllView, AbstractDiaryDaysView,
    AbstractPracticeView, AbstractPrintDiaryView,
    AbstractDayView, AbstractPracticeReviewView,
)


class MindfulnessPracticeAllView(AbstractPracticeAllView):
    """Вывод списка всех практик с осознанностью"""
    Model = MindfulnessPractice


class MindfulnessPracticeView(AbstractPracticeView):
    """Получалка инфы о практике с осознанностью"""
    Model = MindfulnessPractice


class MindfulnessGetAllDiaryDaysView(AbstractDiaryDaysView):
    """Ручка для получения всех дней в дневнике с осознанностью"""
    Model = MindfulnessDiary


class MindfulnessPrintDiaryView(AbstractPrintDiaryView):
    """Ручка для печати дневника с осознанностью"""
    Model = MindfulnessDiary
    StudentModel = MindfulnessStudent


class MindfulnessCreateDiaryView(APIView):
    """Создание нового дневника с осознанностью"""

    def post(self, request):

        practice_id = request.POST.get('practice', None)
        if practice_id is None:
            return Response(status=400, data='No practice in kwargs!')

        practice = MindfulnessPractice.objects.get(id=practice_id)

        if MindfulnessDiary.objects.filter(practice=practice).exists():
            return Response(status=400, data='You have created diary yet!')

        daterange = pd.date_range(practice.date_start, practice.date_end)
        diary = MindfulnessDiary.objects.create()
        days = []
        for day in daterange:
            dday = MindfulnessDiaryDay.objects.create(
                date=day,
                work_info='',
            )
            diary.diary_days.add(dday)

            model_entry = {
                'id': dday.id,
                'date': dday.date,
                'work_info': dday.work_info,
                'is_complete': dday.is_complete,
            }
            days.append(model_entry)

        diary.practice = practice
        diary.save()
        practice.save()
        return Response(status=200, data={'diary_id': diary.id, 'days': days})


class MindfulnessGetDayView(AbstractDayView):
    """Получаем инфу об конкретном дне с осознанностью"""
    Model = MindfulnessDiaryDay


class MindfulnessEditDayView(APIView):
    """Создаем/редактируем инфу об конкретном дне с осознанностью"""

    def post(self, request):

        day_id = request.POST.get('day', None)
        work_info = request.POST.get('work_info', '')
        liked_things = request.POST.get('liked_things', '')
        disliked_things = request.POST.get('disliked_things', '')
        day_evaluation = request.POST.get('day_evaluation', None)

        if day_id is not None:

            # TODO: Сделать покрасивее
            day = MindfulnessDiaryDay.objects.get(id=day_id)
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


class MindfulnessPracticeReviewView(AbstractPracticeReviewView):
    """Ручка для получения всех отзывов о практики с осознанностью"""

    Model = MindfulnessStudentPractice
