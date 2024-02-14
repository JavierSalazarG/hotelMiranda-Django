"""
URL configuration for hotelMiranda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
hola hgola
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from django.views.generic import TemplateView
from db.views.contact import contact
from db.views.about import about
from db.views.rooms import rooms
from db.views.room import Room
from db.views.offers import offers
from db.views.Login import Login
from db.views.Profile import ProfileView 
urlpatterns = [
    path('admindb/', admin.site.urls),
    path('accounts/login/', Login.as_view(), name='login'), 
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'), 
    path('contact/', contact, name='contacts'),
    path('about/', about, name='about'),
    path('rooms/', rooms, name='rooms'),
    path("room/<int:idRoom>/", Room, name="roomDetail"),
    path('offers/', offers, name='offers'),
]
