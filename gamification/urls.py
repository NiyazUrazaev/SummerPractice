from django.urls import path

from gamification.views import *

urlpatterns = [
    path('diary', GamificationGetAllDiaryDaysView.as_view()),
    path('get_day', GamificationGetDayView.as_view()),
    path('edit_day', GamificationEditDayView.as_view()),
    path('all', GamificationPracticeAllView.as_view()),
    path('', GamificationPracticeView.as_view()),
    path('create_diary', GamificationCreateDiaryView.as_view()),
    path('print_diary', GamificationPrintDiaryView.as_view()),
    path('get_reviews', GamificationPracticeReviewView.as_view()),
]
