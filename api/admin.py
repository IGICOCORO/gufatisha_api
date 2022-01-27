from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = "nom","email"
	search_fields = "nom", 

@admin.register(ValeurAjoutee)
class ValeurAjouteeAdmin(admin.ModelAdmin):
	list_display = "nom_valeur",
	search_fields = "nom_valeur", 
    

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
	list_display = "nom_hotel", "photo_couverture", "chambre"
	search_fields = "nom_hotel", 
    

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
	list_display = "numero","nbre_personnes"
	search_fields = "nbre_personnes",

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = "client", "chambre"
	search_fields = "client_fullname", 
