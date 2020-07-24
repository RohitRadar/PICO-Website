from django.db import models

# Create your models here.
class Homepage(models.Model):
	title1 = models.TextField(max_length=50)
	thumb1 = models.ImageField(default='default.png', blank=True)
	title2 = models.TextField(max_length=50, default="title")
	thumb2 = models.ImageField(default='default.png', blank=True)
	title3 = models.TextField(max_length=50, default="title")
	thumb3 = models.ImageField(default='default.png', blank=True)
	title4 = models.TextField(max_length=50, default="title")
	thumb4 = models.ImageField(default='default.png', blank=True)
	title5 = models.TextField(max_length=50, default="title")
	thumb5 = models.ImageField(default='default.png', blank=True)
	title6 = models.TextField(max_length=50, default="title")
	thumb6 = models.ImageField(default='default.png', blank=True)

def __str__(self):
	return self.title