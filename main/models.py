from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    organization = models.CharField(max_length=32, default="Daily Bruin")
    # title = models.CharField(max_length=32)
    email = models.EmailField()
    twitter = models.CharField(max_length=15) # current max handle length
    facebook = models.CharField(max_length=32)
    mug = models.ImageField(upload_to='mug/%Y')
    bio = models.TextField()
