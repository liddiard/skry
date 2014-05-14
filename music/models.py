from django.db import models

class Album(models.Model):	
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=64)
    rating = models.IntegerField()
    review_url = models.URLField()
    author = models.ForeignKey('main.Author')
    artwork = models.ImageField(upload_to='music/')
    spotify_url = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.title

