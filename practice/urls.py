from django.urls import path

from practice.views import *

urlpatterns = [
    path('diary', DiaryView.as_view()),
    path('day', DayView.as_view()),
    path('all', PracticeAllView.as_view()),
    path('', PracticeView.as_view()),
    path('review', PracticeReviewView.as_view()),
]
