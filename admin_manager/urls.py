from django.contrib import admin
from django.urls import path, include

from . import views
from chat.views import chat
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notfound/', views.Notfound,name='Notfound'),
    path('chat/',include('chat.urls')),
    path('', include('authentication.url')),
]
