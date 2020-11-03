from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
