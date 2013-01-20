from django.db import models

# Create your models here.
class Description(models.Model):
	"""Introduction to the company."""

	text = models.TextField()

	def __unicode__(self):
		return self.text


class Philosophy(models.Model):
	"""Philosophies that we try to embody."""

	title = models.CharField(max_length=256)
	text = models.TextField()
	order = models.IntegerField(unique=True, null=True, blank=True)

	def __unicode__(self):
		return self.title


class TechnicalSkill(models.Model):
	"""Techcnical skills that we possess."""

	title = models.CharField(max_length=256)
	text = models.TextField()
	order = models.IntegerField(unique=True, null=True, blank=True)
	icon = models.ImageField(upload_to='technical_skills_images')

	def __unicode__(self):
		return self.title
