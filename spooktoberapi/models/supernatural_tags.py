from django.db import models


class SupernaturalTags(models.Model):
    """Supernatural Model
    Fields:
    
    """
    movie_tv = models.ForeignKey("Movie_Tv", on_delete=models.CASCADE)
    supernatural = models.ForeignKey("Supernatural", on_delete=models.CASCADE) 