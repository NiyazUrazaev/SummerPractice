from django.urls import path

from practice.views import *

urlpatterns = [
    path('get_all_days', ClassicGetAllDiaryDaysView.as_view()),
    path('get_day', ClassicGetDayView.as_view()),
    path('edit_day', ClassicEditDayView.as_view()),
    path('all', ClassicPracticeAllView.as_view()),
    path('student_all', ClassicStudentPracticeAllView.as_view()),
    path('', ClassicPracticeView.as_view()),
    path('create_diary', ClassicCreateDiaryView.as_view()),
    path('print_diary', ClassicPrintDiaryView.as_view()),
]
