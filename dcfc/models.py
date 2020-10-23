from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
        

class Blog(models.Model):
    title = models.CharField(max_length =60)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to= 'pics/', default = 'TRUE')

    def __str__(self):
        return self.title

    @classmethod
    def search_by_content(cls,search_term):
        church = cls.objects.filter(title__icontains=search_term)
        return church

class Video(models.Model):
    title= models.CharField(max_length=50)
    link = models.URLField(blank=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()