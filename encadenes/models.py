from django.db import models
from django.utils import timezone

class Country(models.Model):
	country = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.country

class States(models.Model):
	state = models.CharField(max_length=100)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	def __str__(self):
		return self.States

class Crags(models.Model):
	crag  = models.CharField(max_length=100, unique=True)
	state = models.ForeignKey(States, on_delete=models.CASCADE)
	def __str__(self):
		return self.crag

class Sectors(models.Model):
	sector = models.CharField(max_length=100, unique=True)
	crag = models.ForeignKey(Crags, on_delete=models.CASCADE)
	total_routes = models.IntegerField(default=0)
	def __str__(self):
		return self.sector

class Routes(models.Model):
	route = models.CharField(max_length=100, unique=True)
	rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
	total_ascents = models.IntegerField(default=0)
	recommended_by = models.IntegerField(default=0)
	sector = models.ForeignKey(Crags, on_delete=models.CASCADE)
	grado = models.CharField(max_length=10, default='000')
	def __str__(self):
		return self.route
