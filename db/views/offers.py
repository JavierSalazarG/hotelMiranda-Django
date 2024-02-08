from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from db.models import Rooms
def offers(request):
    discounted_rooms = Rooms.objects.filter(offerPrice__lt=F('rate'))
    return render(
        request,
        "../templates/offers.html",
        {"rooms": discounted_rooms}
)