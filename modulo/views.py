from django.shortcuts import render


def login(request):
    return render(request, 'modulo/login.html')


def index(request):
    return render(request, 'modulo/index.html')


def room(request, room_name):
    return render(request, 'modulo/room.html', {
        'room_name': room_name
    })
