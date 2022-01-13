from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Client(models.Model):
	fullname = models.CharField(max_length=30)
	email = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.fullname} {self.email}"

class Hotel(models.Model):
	nom = models.CharField(max_length=30,blank=False)
	photo_couverture = models.ImageField()
	chambre = models.ForeignKey("Chambre",on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.nom} {self.photo_couverture}"

class ValeurAjoutee(models.Model):
	hotel_id= models.ForeignKey(Hotel,on_delete=models.PROTECT)
	nom_valeur = models.CharField(max_length=30)

	def __str__(self):
		return self.nom_valeur

class Chambre(models.Model):
	type_chambre = models.CharField(max_length=30)
	numero = models.PositiveBigIntegerField( default=0 )
	pic_chambr1 = models.ImageField()
	pic_chambr2 = models.ImageField()
	pic_chambr3 = models.ImageField()
	nbre_personnes = models.PositiveSmallIntegerField()
	

	def __str__(self):
		return f"{self.numero} { self.type_chambre} "

class Reservation(models.Model):
	date_arrivee = models.DateField()
	date_depart = models.DateField()
	client = models.ForeignKey(Client, on_delete=models.PROTECT)
	chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
	reservee = models.BooleanField()

	def __str__(self):
		return f"chambre N° {self.numero} est reservé du { self.date_arrivee} au { self.date_depart} par {self.client_fullname} "