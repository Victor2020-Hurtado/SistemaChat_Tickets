from django.shortcuts import render


def dashboard(request):
    return render(request, 'modulo/dashboard.html')


def tickets(request):
    return render(request, 'modulo/tickets.html')


def chat(request):
    return render(request, 'modulo/chat.html')


def room(request, room_name):
    return render(request, 'modulo/room.html', {
        'room_name': room_name
    })
