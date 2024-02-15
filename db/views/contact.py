from django.shortcuts import render
from django.http import HttpResponse
from db.models import Contact
def contact(request):
    success_message = None
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email_address = request.POST.get('email_address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(foto_perfil='https://d500.epimg.net/cincodias/imagenes/2016/07/04/lifestyle/1467646262_522853_1467646344_noticia_normal.jpg' , nombre=full_name, email=email_address, phone=phone_number, comentario=message, archive=0)
        contact.save()
        success_message = 'Mensaje enviado exitosamente' 
    return render(request, "contacts.html", {'success_message': success_message})