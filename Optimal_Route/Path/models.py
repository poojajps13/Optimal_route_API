from django.db import models

# Create your models here.
class Deliveries(models.Model):
	name = models.CharField(max_length=200)
	address = models.TextField(max_length=1000)
	lat = models.CharField(max_length= 100)
	lng = models.CharField(max_length= 100)
	delivery_date = models.DateField()
	status = models.CharField(max_length=20)
	def __str__(self):
		return self.name