from django.db import models


class UserCal(models.Model):
    """UserCal Model
    Fields:
    
    """
    movie_tv= models.ForeignKey("Movie_Tv", on_delete=models.CASCADE)
    selected = models.DateField()


    