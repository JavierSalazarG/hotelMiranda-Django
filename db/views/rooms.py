from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from db.models import Rooms
def rooms(request):
    all_rooms = Rooms.objects.all()
    return render(
        request,
        "../templates/rooms.html",
        {'rooms': all_rooms} 
)

def roomId(request, idRoom):
    room = get_object_or_404(Rooms, id=idRoom)
    all_rooms = Rooms.objects.all()
    return render(
        request,
        "../templates/room.html",
        {'room': room, 'rooms': all_rooms}
    )