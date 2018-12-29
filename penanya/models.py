from django.db import models
from django.utils.text import slugify

# Create your models here.

class Penanya(models.Model):
	nama = models.CharField(max_length=50)
	kategoriPertanyaan = models.CharField(max_length=50)
	babPertanyaan = models.CharField(max_length=50)
	asalSekolah = models.CharField(max_length=50)
	minat = models.CharField(max_length=50)
	waktubertanya = models.DateTimeField(auto_now_add=True)
	foto_profil = models.ImageField()
	slug = models.SlugField(editable=False, blank=True)

	def save(self):
		self.slug = slugify(self.kategoriPertanyaan)
		super(Penanya, self).save()
	
	def __str__(self):
		return "{}".format(self.nama)