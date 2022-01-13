from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = "fullname","email"
	search_fields = "fullname", 

@admin.register(ValeurAjoutee)
class ValeurAjouteeAdmin(admin.ModelAdmin):
	list_display = "hotel_id", "nom_valeur"
	search_fields = "hotel_id", 
    

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
	list_display = "nom", "photo_couverture", "chambre"
	search_fields = "nom", 
    

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
	list_display = "numero","nbre_personnes"
	search_fields = "nbre_personnes",

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = "client", "chambre"
	search_fields = "client_fullname", 
