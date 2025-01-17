"""
URL configuration for theme_entertainment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.theme_list, name='theme_list'),
    path('create/', views.theme_create, name='theme_create'),
    path('activity_management/', views.activity_management,
         name='activity_management'),
    path('api/events/', views.get_events, name='get_events'),
    path('api/events/<str:event_id>/',
         views.get_event_detail, name='get_event_detail'),
]
