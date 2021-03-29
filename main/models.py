from django.db import models
from django.contrib.auth.models import User



class Contact(models.Model):

	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	name = models.CharField(verbose_name="Name",max_length=100)
	telephone = models.CharField(max_length=15)
	email = models.EmailField(verbose_name="Email")
	message = models.CharField(verbose_name="Message",max_length=1000)
	captcha_score = models.FloatField(default = 0.0)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return f'{self.name}'