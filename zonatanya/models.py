from django.db import models
from django.utils.text import slugify


class Pertanyaan(models.Model):

	mata_pelajaran 	= models.CharField(max_length=25)
	bab				= models.CharField(max_length=25)
	pertanyaan 		= models.CharField(max_length=300)
	slug			= models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug 	= slugify(self.mata_pelajaran)
		super(Pertanyaan, self).save()

	def __str__(self):
		return "{} - {}".format(self.mata_pelajaran, self.bab)