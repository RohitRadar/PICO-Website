from django.db import models

# Create your models here.
class photogallery(models.Model):
	text = models.TextField(max_length=80, default="Type only 1 line for display in product box")
	thumb = models.ImageField(default='default.png', blank=True)


	def __str__(self):
		return self.text