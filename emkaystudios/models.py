from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
	title = models.CharField(max_length=128)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title