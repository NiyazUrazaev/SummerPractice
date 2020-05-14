# -*- coding: utf-8 -*-

import pandas as pd
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response

from practice.abstract_views import (
    AbstractPracticeAllView, AbstractDiaryDaysView,
    AbstractPracticeView, AbstractPrintDiaryView,
    AbstractDayView,
)
from practice.models import (
    ClassicPractice, ClassicDiary,
    ClassicDiaryDay,
)
from user.models import ClassicStudent


class ClassicPracticeAllView(AbstractPracticeAllView):
    """Вывод списка всех классических практик"""
    Model = ClassicPractice


class ClassicPracticeView(AbstractPracticeView):
    """Получалка инфы о классической практике"""
    Model = ClassicPractice


class ClassicGetAllDiaryDaysView(AbstractDiaryDaysView):
    """Ручка для получения всех классических дней в дневнике"""
    Model = ClassicDiary


class ClassicPrintDiaryView(AbstractPrintDiaryView):
    """Ручка для печати классического дневника"""
    Model = ClassicDiary
    StudentModel = ClassicStudent


class ClassicCreateDiaryView(APIView):
    """Создание нового классического дневника"""

    def post(self, request):

        practice_id = request.POST.get('practice_id', None)
        if practice_id is None:
            return Response(status=400, data='No practice_id in kwargs!')

        practice = ClassicPractice.objects.get(id=practice_id)

        if ClassicDiary.objects.filter(practice=practice).exists():
            return Response(status=400, data='You have created diary yet!')

        daterange = pd.date_range(practice.date_start, practice.date_end)
        diary = ClassicDiary.objects.create()
        days = []
        for day in daterange:
            dday = ClassicDiaryDay.objects.create(
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


class ClassicGetDayView(AbstractDayView):
    """Получаем инфу об конкретном классическом дне"""
    Model = ClassicDiaryDay


class ClassicEditDayView(APIView):
    """Создаем/редактируем инфу об конкретном классическом дне"""

    def post(self, request):

        day_id = request.POST.get('day_id', None)
        work_info = request.POST.get('work_info', '')

        if day_id is not None:

            # TODO: Сделать покрасивее
            day = ClassicDiaryDay.objects.get(id=day_id)
            day.work_info = work_info
            if work_info != '':
                day.is_complete = True
            day.save()

            return Response(
                status=200,
                data=model_to_dict(day)
            )
        else:
            return Response(status=400, data='No day_id in kwargs!')
