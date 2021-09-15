from django.db import models


class Movie_Tv(models.Model):
    """Movie_Tv Model
    Fields:
    
    """
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=150)
    subGenre = models.CharField(max_length=150)
    spirit = models.CharField(max_length=150)
    era = models.CharField(max_length=150)
    isMovie = models.BooleanField()
    isNostalgic = models.BooleanField()
    isMagic = models.BooleanField()
    isTimBurton = models.BooleanField()
    isStopMotion = models.BooleanField()
    imdb_img = models.URLField()
    imdb_rating = models.IntegerField()
    supernatural = models.ManyToManyField("Supernatural", through="SupernaturalTags")
