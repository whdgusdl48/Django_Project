from django.db import models

# Create your models here.
class BoardData(models.Model):
    title = models.CharField(max_length=300)
    ranking = models.IntegerField(default=0)
    imgurl = models.URLField()
    artist = models.CharField(max_length=200)
