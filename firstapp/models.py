from django.db import models

# Create your models herec

class firstapp_model(models.Model):
	name = models.CharField(max_length = 200)
	age = models.CharField(max_length=100)
	
	def __str__(self):
		return f"{self.name} and {self.age}"