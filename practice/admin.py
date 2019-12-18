# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from practice.models import Practice, Diary, DiaryDay

admin.site.register(DiaryDay)
admin.site.register(Diary)
admin.site.register(Practice)