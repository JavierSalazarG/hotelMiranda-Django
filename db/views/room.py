from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from db.models import Booking, Rooms


def Room(request, idRoom):
    room = get_object_or_404(Rooms, id=idRoom)
    all_rooms = Rooms.objects.all()
    success_message = ''
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        name = request.POST.get('name')
        nota = request.POST.get('note')
        id_habitacion = room
        status = 'confirmed'
        
        booking = Booking.objects.create(name=name, check_in=check_in, check_out=check_out, nota=nota, id_habitacion=id_habitacion, status=status)
        booking.save()
        success_message = "¡Formulario enviado exitosamente!"   
    return render(request, "room.html", {'room': room, 'rooms': all_rooms, 'success_message': success_message})