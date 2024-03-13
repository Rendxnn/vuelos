from django.db import models

class Vuelo(models.Model):
	nombre = models.CharField(max_length=255)
	tipo = models.CharField(max_length=20)
	precio = models.DecimalField(max_digits=10, decimal_places=2)

