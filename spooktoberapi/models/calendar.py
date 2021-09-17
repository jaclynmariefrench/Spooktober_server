from django.db import models


class UserCal(models.Model):
    """UserCal Model
    Fields:
    
    """
    # Need to change many to many
    movie_tv= models.ForeignKey("movie_tv", on_delete=models.CASCADE)
    selected = models.DateField()


    