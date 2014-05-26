from django.db import models

# Create your models here.

class Reporter(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateField()
	content = models.TextField()
	reporte = models.ForeignKey(Reporter)

	def __unicode__(self):
		return self.title