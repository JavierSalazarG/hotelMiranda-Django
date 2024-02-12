from django.db import models

class Contact(models.Model):
    foto_perfil = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=9)
    comentario = models.TextField()
    archive = models.BooleanField()
    def __str__(self):
        return self.nombre


class Rooms(models.Model):
    roomNumber = models.IntegerField()
    img = models.CharField(max_length=255)
    bedType = models.CharField(max_length=255)
    facilities = models.JSONField()
    rate = models.FloatField()
    offerPrice = models.FloatField()
    status = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    

class Booking(models.Model):
    name = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()
    nota = models.TextField()
    id_habitacion = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    
    