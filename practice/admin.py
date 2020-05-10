# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from practice.models import ClassicPractice, ClassicDiary, ClassicDiaryDay

admin.site.register(ClassicDiary)
admin.site.register(ClassicDiaryDay)
admin.site.register(ClassicPractice)