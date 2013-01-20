from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	"""Blog posts"""
	title = models.CharField(max_length=256)
	text = models.TextField()
	author = models.ForeignKey(User)
	created_on = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.title