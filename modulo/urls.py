from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tickets/', views.tickets, name='tickets'),
    path('chat/', views.chat, name='chat'),
    path('<str:room_name>/', views.room, name='room'),
]
