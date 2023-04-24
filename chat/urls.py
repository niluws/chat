from django.urls import path

from .views import chat,room,chat_list

urlpatterns = [
    path('', chat, name='home'),
    path('chat_list/', chat_list, name='chat_list'),
    path('<str:room_name>/', room,name='room'),
]
