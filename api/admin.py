from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = "fullname","email"
	search_fields = "fullname", 

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
	list_display = "nom", "photo_couverture", "chambre"
	search_fields = "nom", 
    
@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
	list_display = "numero","pic_chambr1", "pic_chambr2", "pic_chambr3", "date_arrivee", "date_depart", "nbre_personnes","reservee"
	search_fields = "nbre_personnes",

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = "client", "chambre"
	search_fields = "client_fullname", 
