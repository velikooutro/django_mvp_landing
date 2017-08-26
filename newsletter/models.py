from django.db import models
import datetime

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120,blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(blank=True, null=True,default=datetime.date.today)

	def __unicode__(self):
		return self.email
