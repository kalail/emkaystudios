from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=128)
	body = models.TextField()
	user = models.ForeignKey(User)
	created_on = models.DateTimeField(auto_now_add=True)

	@property
	def slug(self):
		return slugify(self.title)


	def __unicode__(self):
		return self.title