from django.shortcuts import render
from django.http import HttpResponse
from db.models import Rooms
def rooms(request):
    all_rooms = Rooms.objects.all()
    return render(
        request,
        "../templates/rooms.html",
        {'rooms': all_rooms} 
)