from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = "nom","prenom","provenance","phone","email",
	search_fields =  "nom","prenom","provenance","phone"

@admin.register(ValeurAjoutee)
class ValeurAjouteeAdmin(admin.ModelAdmin):
	list_display = "nom_valeur",
	search_fields = "nom_valeur", 
    

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
	list_display = "nom", "photo_couverture"
	search_fields = "nom", 
    

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
	list_display = "numero","nbre_personnes","type_chambre","prix"
	search_fields = "nbre_personnes","type_chambre","prix"

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = "client", "chambre","date_arrivee","date_depart"
	search_fields = "date_arrivee", 
