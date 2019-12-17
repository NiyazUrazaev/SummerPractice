# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from user.models import Student, Teacher

admin.site.register(Student)
admin.site.register(Teacher)