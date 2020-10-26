from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Gallery(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Article(models.Model):
	title = models.CharField(max_length=200)
	preview = models.TextField(max_length=500)
	content = models.TextField(max_length=1000)
	posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Video(models.Model):
    title= models.CharField(max_length=50)
    link = models.URLField(blank=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
