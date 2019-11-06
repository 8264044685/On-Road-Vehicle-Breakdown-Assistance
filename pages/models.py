from django.db import models

# Create your models here.

class ContactUs(models.Model):
	name = models.CharField(max_length = 255,blank=True)
	subject = models.CharField(max_length=255,blank=True)
	email= models.CharField(max_length=255,blank=True)
	message=models.TextField()
	
	def __str__(self):
		return self.name
    