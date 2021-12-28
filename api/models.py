from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Hotel(models.Model):
	nom = models.CharField(max_length=30,blank=False)
	photo_couverture = models.ImageField()
	chambre = models.ForeignKey("Chambre",on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.nom} {self.photo_couverture}"

class Chambre(models.Model):
	pic_chambr1 = models.ImageField()
	pic_chambr2 = models.ImageField()
	pic_chambr3 = models.ImageField()
	date_arrivee = models.DateField()
	date_depart = models.DateField()
	nbre_personnes = models.PositiveSmallIntegerField()

	def __str__(self):
		return f"Reservé du { self.date_arrivee} au { self.date_depart} "

class Reservation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.user.first_name} {self.chambre}"