from django.shortcuts import render,redirect,reverse


def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    else:
        return render(request, 'chat/chat.html')


def Notfound(request):
    return render(request, 'share/404.html')
