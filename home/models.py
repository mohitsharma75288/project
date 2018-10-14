from django.db import models

# Create your models here.
class question(models.Model):
	name=models.CharField(max_length=200)
	dob=models.DateTimeField('date of birth')
	gender=models.CharField(max_length=200)
	hobbies=models.CharField(max_length=200)
	adress=models.CharField(max_length=200)
	city=models.CharField(max_length=200)
	aimage=models.CharField(max_length=200)

	
