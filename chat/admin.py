from django.contrib import admin

from .models import Message, Chat

admin.site.register(Chat)


@admin.register(Message)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['content']
    ordering = ['-timestamp']
