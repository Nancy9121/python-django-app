from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Crop_Details(models.Model):
	crop_name=models.CharField(max_length=20)
	crop_post_harvest=models.CharField(max_length=25)
	crop_market=models.DecimalField(max_digits=9, decimal_places=2)
	crop_risks=models.TextField()

	def __str__(self):
		return self.crop_name


class User_Details(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateTimeField(default=datetime.now, blank=True)
    salary=models.DecimalField(max_digits=9, decimal_places=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
    	return str(self.user)


