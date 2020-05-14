# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from mindfulness.models import (
    MindfulnessStudent, MindfulnessDiary,
    MindfulnessPractice, MindfulnessDiaryDay,
    MindfulnessStudentPractice
)

admin.site.register(MindfulnessStudent)
admin.site.register(MindfulnessDiary)
admin.site.register(MindfulnessDiaryDay)
admin.site.register(MindfulnessPractice)
admin.site.register(MindfulnessStudentPractice)
