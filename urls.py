from django.urls import path
from . import views

app_name = 'theme_entertainment'

urlpatterns = [
    path('list/', views.theme_list, name='theme_list'),
    path('create/', views.theme_create, name='theme_create'),
    path('management/', views.activity_management, name='activity_management'),
    path('api/events/', views.get_events, name='get_events'),
    path('api/events/<str:event_id>/',
         views.get_event_detail, name='get_event_detail'),
]
