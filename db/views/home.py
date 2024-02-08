from django.shortcuts import render
from db.models.form import inputForCheck

def home(request):
   
    return render(
        request,
        "../templates/index.html",
        
    )