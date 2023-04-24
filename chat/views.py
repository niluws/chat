import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Chat


# user = get_user_model()
@login_required(login_url='login')
def chat(request):
    user = request.user
    chat_rooms = Chat.objects.filter(members=user).prefetch_related('message_set')

    return render(request, 'chat/chat.html', {'chat_rooms': chat_rooms})


@login_required(login_url='login')
def room(request, room_name):
    user = request.user
    chat_model = Chat.objects.filter(roomname=room_name)
    if not chat_model.exists():
        chat = Chat.objects.create(roomname=room_name)
        chat.members.add(user)
    else:
        chat_model[0].members.add(user)
    username = request.user.username
    userid = str(request.user.id)
    context = {
        "room_name": room_name,
        'userid': mark_safe(json.dumps(userid)),
        'username': mark_safe(json.dumps(username))

    }

    return render(request, 'chat/room.html', context)


@login_required(login_url='login')
def chat_list(request):
    user = request.user
    chat_rooms = Chat.objects.filter(members=user).prefetch_related('message_set')

    return render(request, 'chat/chat_list.html', {'chat_rooms': chat_rooms})
