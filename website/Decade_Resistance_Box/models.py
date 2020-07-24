from django.db import models

# Create your models here.
class Decade_Resistance_Box(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(default="This is the URL")
	snippet1 = models.TextField(max_length=80, default="Type only 1 line for display in product box")
	snippet2 = models.TextField(max_length=80, default="Type only 1 line for display in product box")
	snippet3 = models.TextField(max_length=80, default="Type only 1 line for display in product box")
	file = models.FileField(default="default.pdf")
	thumb = models.ImageField(default='default.png', blank=True)


	def __str__(self):
		return self.title