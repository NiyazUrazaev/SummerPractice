"""SummerPractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from SummerPractice.settings import INSTALLED_APPS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('classic_practice/', include('practice.urls')),
]

if 'gamification' in INSTALLED_APPS:
    urlpatterns.append(path('gamification_practice/', include('gamification.urls')))
if 'mindfulness' in INSTALLED_APPS:
    urlpatterns.append(path('mindfulness_practice/', include('mindfulness.urls')))
