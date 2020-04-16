# -*- coding: utf-8 -*-

from django.forms.models import model_to_dict
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response

from practice.diary_docx.api import DocxDiary
from user.models import Student, StudentPractice
from .models import Diary, DiaryDay, Practice


class PracticeAllView(APIView):

    # Вывод списка всех практик
    def get(self, request):
        practices = [
            model_to_dict(practice)
            for practice in Practice.objects.all().select_related(
                'teacher',)
        ]

        return Response(status=200, data=practices)


class PracticeView(APIView):

    # Получалка инфы о практике
    def get(self, request):
        practice_id = request.GET.get('id', None)
        if practice_id is None:
            return Response(status=400, data='No id in kwargs!')
        practice = Practice.objects.get(id=practice_id)

        return Response(status=200, data=model_to_dict(practice))


class PracticeReviewView(APIView):

    # Получаем все отзывы по практике
    def get(self, request):
        practice_id = request.GET.get('id', None)
        if practice_id is None:
            return Response(status=400, data='No id in kwargs!')
        reviews = StudentPractice.objects.filter(
            practice__id=practice_id).values_list('student__id', 'review')

        return Response(status=200, data=reviews)

    # Студент оставляет отзыв практике
    def post(self, request):
        practice_id = request.POST.get('id', None)
        if practice_id is None:
            return Response(status=400, data='No id in kwargs!')
        # TODO доделать после авторизации
        student = request.user


class DiaryView(APIView):

    def get(self, request):
        diary_id = request.GET.get('diary', None)
        if diary_id is None:
            return Response(status=400, data='No diary in kwargs!')

        diary = Diary.objects.get(id=diary_id)
        diary_days = diary.diary_days.all().order_by('date')

        days = []
        for day in diary_days:
            model_entry = {
                'id': day.id,
                'date': day.date,
                'work_info': day.work_info,
                'is_complete': day.is_complete,
                'liked_things': day.liked_things,
                'disliked_things': day.disliked_things,
                'day_evaluation': day.day_evaluation,
            }
            days.append(model_entry)

        return Response(status=200, data=days)

    def post(self, request):
        print(request.POST)
        diary_id = request.POST.get('diary', None)
        # Значит создаем новый
        if diary_id is None:
            practice_id = request.POST.get('practice', None)
            if practice_id is None:
                return Response(status=400, data='No practice in kwargs!')

            practice = Practice.objects.get(id=practice_id)
            daterange = pd.date_range(practice.date_start, practice.date_end)
            diary = Diary.objects.create()
            days = []
            for day in daterange:
                dday = DiaryDay.objects.create(
                    date=day,
                    work_info='',
                    is_complete=False,
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

        # Если пришли сюда - генерим док
        diary = Diary.objects.get(id=diary_id)
        diary_days = diary.diary_days.filter(is_complete=True).order_by('date')
        practice = diary.practice
        student = Student.objects.get(practices=practice)

        diary_docx = DocxDiary(
            student,
            practice.teacher,
            practice,
            diary_days,
        )

        download_url = diary_docx.create_docx()

        return Response(status=200, data=download_url)


class DayView(APIView):

    def get(self, request):
        day_id = request.GET.get('day', None)
        if day_id is None:
            return Response(status=400, data='No day in kwargs!')

        day = DiaryDay.objects.get(id=day_id)

        return Response(
            data={
                'id': day.id,
                'date': day.date,
                'work_info': day.work_info,
                'is_complete': day.is_complete,
                'liked_things': day.liked_things,
                'disliked_things': day.disliked_things,
                'day_evaluation': day.day_evaluation,
            }
        )

    def post(self, request):

        day_id = request.POST.get('day', None)
        work_info = request.POST.get('work_info', '')
        liked_things = request.POST.get('liked_things', '')
        disliked_things = request.POST.get('disliked_things', '')
        day_evaluation = request.POST.get('day_evaluation', None)

        if day_id is not None:

            # TODO: Сделать покрасивее
            day = DiaryDay.objects.get(id=day_id)
            day.work_info=work_info
            if work_info != '':
                day.is_complete = True
            day.liked_things=liked_things
            day.disliked_things=disliked_things
            day.day_evaluation=day_evaluation
            day.save()

            return Response(
                status=200,
                data={
                    'message': 'Edit is success!',
                    'id': day.id,
                    'date': day.date,
                    'work_info': day.work_info,
                    'is_complete': day.is_complete,
                    'liked_things': day.liked_things,
                    'disliked_things': day.disliked_things,
                    'day_evaluation': day.day_evaluation,
                }
            )
        else:
            return Response(status=400, data='No day in kwargs!')

