from django.urls import path

from mindfulness.views import *

urlpatterns = [
    path('diary', MindfulnessGetAllDiaryDaysView.as_view()),
    path('get_day', MindfulnessGetDayView.as_view()),
    path('edit_day', MindfulnessEditDayView.as_view()),
    path('all', MindfulnessPracticeAllView.as_view()),
    path('', MindfulnessPracticeView.as_view()),
    path('create_diary', MindfulnessCreateDiaryView.as_view()),
    path('print_diary', MindfulnessPrintDiaryView.as_view()),
    path('get_reviews', MindfulnessPracticeReviewView.as_view()),
]