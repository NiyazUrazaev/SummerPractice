# -*- coding: utf-8 -*-

from django.shortcuts import render
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Diary, DiaryDay


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
                # 'work_info': day.work_info,
            }
            days.append(model_entry)

        return Response(status=200, data=days)


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
            }
        )

    def post(self, request):
        day_id = request.POST.get('day', None)
        date = request.POST.get('date', None)
        work_info = request.POST.get('work_info', None)
        if day_id is not None:
            day = DiaryDay.objects.get(id=day_id)
            day.date = datetime.datetime.strptime(date, '%Y%m%d').date()
            day.work_info=work_info
            day.save()

            return Response(
                status=200,
                data={
                    'message': 'Edit is succes!',
                    'id': day.id,
                    'date': day.date,
                    'work_info': day.work_info,
                })
        else:
            day = DiaryDay.objects.create(
                date=datetime.datetime.strptime(date, '%Y%m%d').date(),
                work_info=work_info
            )

        return Response(
            status=200,
            data={
                'message': 'Save new day is succes!',
                'id': day.id,
                'date': day.date,
                'work_info': day.work_info,
            })
