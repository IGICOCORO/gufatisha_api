from django.db import models

# Create your models here.

class Client(models.Model):
	id 	 = models.AutoField(primary_key=True)
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	provenance = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	email = models.EmailField()

	def __str__(self):
		return f"{self.nom} {self.prenom} {self.provenance} {self.phone} {self.email}"

class Hotel(models.Model):
	id 	 = models.AutoField(primary_key=True)
	nom = models.CharField(max_length=30,blank=False)
	photo_couverture = models.ImageField(upload_to='media/')
	
	def __str__(self):
		return f"{self.nom} {self.photo_couverture}"

class ValeurAjoutee(models.Model):
	id 	 = models.AutoField(primary_key=True)
	nom_valeur = models.CharField(max_length=30)
	hotel = models.ForeignKey("Hotel",on_delete=models.PROTECT)


	def __str__(self):
		return self.nom_valeur

class Chambre(models.Model):
	id 	 = models.AutoField(primary_key=True)
	type_chambre = models.CharField(max_length=30)
	numero = models.PositiveBigIntegerField( default=0 )
	pic_chambr1 = models.ImageField(upload_to='media/')
	pic_chambr2 = models.ImageField(upload_to='media/')
	pic_chambr3 = models.ImageField(upload_to='media/')
	nbre_personnes = models.PositiveSmallIntegerField()
	prix = models.PositiveIntegerField(default=0)
	hotel = models.ForeignKey("Hotel",on_delete=models.PROTECT)
	

	def __str__(self):
		return f"{self.numero} { self.type_chambre} "

class Reservation(models.Model):
	id 	 = models.AutoField(primary_key=True)
	date_arrivee = models.DateField()
	date_depart = models.DateField()
	client = models.ForeignKey(Client, on_delete=models.PROTECT)
	chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)

	def __str__(self):
		return f"chambre N° {self.numero} est reservé du { self.date_arrivee} au { self.date_depart} par {self.nom} {self.prenom} "