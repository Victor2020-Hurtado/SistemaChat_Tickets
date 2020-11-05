from django.shortcuts import render


def login(request):
    return render(request, 'modulo/login.html')


def dashboard(request):
    return render(request, 'modulo/dashboard.html')


def room(request, room_name):
    return render(request, 'modulo/room.html', {
        'room_name': room_name
    })
