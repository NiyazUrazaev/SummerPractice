from abc import ABC

from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from practice.diary_docx.api import DocxDiary


class SetModelMixin:

    @property
    def Model(self):
        raise NotImplementedError


class AbstractPracticeAllView(APIView, SetModelMixin, ABC):
    """Вывод списка всех практик"""

    def get(self, request):
        practices = [
            model_to_dict(practice)
            for practice in type(self).Model.objects.all().select_related(
                'teacher', )
        ]

        return Response(status=200, data=practices)


class AbstractPracticeView(APIView, SetModelMixin, ABC):
    """Получалка инфы о практике"""

    def get(self, request):
        practice_id = request.GET.get('id', None)
        if practice_id is None:
            return Response(status=400, data='No id in kwargs!')
        practice = type(self).Model.objects.get(id=practice_id)

        return Response(status=200, data=model_to_dict(practice))


class AbstractPracticeReviewView(APIView, SetModelMixin, ABC):

    # Получаем все отзывы по практике
    def get(self, request):

        practice_id = request.GET.get('id', None)
        if practice_id is None:
            return Response(status=400, data='No id in kwargs!')
        reviews = type(self).Model.objects.filter(
            practice__id=practice_id).values_list('student__id', 'review')

        return Response(status=200, data=reviews)

    # Студент оставляет отзыв практике
    def post(self, request):

        practice_id = request.POST.get('id', None)
        if practice_id is None:
            return Response(status=400, data='No id in kwargs!')
        # TODO доделать после авторизации
        student = request.user


class AbstractDiaryDaysView(APIView, SetModelMixin, ABC):
    """Абстрактная ручка для получения всех дней в дневнике"""

    def get(self, request):
        diary_id = request.GET.get('diary', None)
        if diary_id is None:
            return Response(status=400, data='No diary in kwargs!')

        diary = type(self).Model.objects.get(id=diary_id)
        diary_days = diary.diary_days.all().order_by('date')

        days = [model_to_dict(day) for day in diary_days]

        return Response(status=200, data=days)


class AbstractPrintDiaryView(APIView, SetModelMixin, ABC):
    """Абстрактная ручка для печати дневника"""

    @property
    def StudentModel(self):
        raise NotImplementedError

    def post(self, request):
        diary_id = request.POST.get('diary', None)
        if diary_id is None:
            return Response(status=400, data='No diary in kwargs')

        diary = type(self).Model.objects.get(id=diary_id)
        diary_days = diary.diary_days.filter(is_complete=True).order_by('date')
        practice = diary.practice
        # FIXME: Возможно неправильно беру студента
        student = type(self).StudentModel.objects.get(practices=practice)

        diary_docx = DocxDiary(
            student,
            practice.teacher,
            practice,
            diary_days,
        )

        download_url = diary_docx.create_docx()

        return Response(status=200, data=download_url)


class AbstractDayView(APIView, SetModelMixin, ABC):
    """Получаем инфу об конкретном дне"""

    def get(self, request):
        day_id = request.GET.get('day', None)
        if day_id is None:
            return Response(status=400, data='No day in kwargs!')

        day = type(self).Model.objects.get(id=day_id)

        return Response(
            status=200,
            data={
                model_to_dict(day)
            }
        )
