from django.db import models
from django.utils import timezone

class Country(models.Model):
	country = models.CharField(max_length=100)

class States(models.Model):
	state = models.CharField(max_length=100)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Crags(models.Model):
	crag  = models.CharField(max_length=100)
	state = models.ForeignKey(States, on_delete=models.CASCADE)

class Sectors(models.Model):
	sector = models.CharField(max_length=100)
	crag = models.ForeignKey(Crags, on_delete=models.CASCADE)
	total_routes = models.IntegerField()

class Routes(models.Model):
	route = models.CharField(max_length=100)
	rating = models.DecimalField(max_digits=3, decimal_places=2)
	total_ascents = models.IntegerField()
	recommended_by = models.IntegerField()
	sector = models.ForeignKey(Crags, on_delete=models.CASCADE)
