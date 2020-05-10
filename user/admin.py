# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from user.models import ClassicStudent, Teacher

admin.site.register(ClassicStudent)
admin.site.register(Teacher)