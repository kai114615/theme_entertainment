from django.urls import path
from . import views

app_name = 'theme_entertainment'

urlpatterns = [
    path('events/', views.get_entertainment_events, name='entertainment_events'),
]
