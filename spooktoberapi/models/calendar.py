from django.db import models
from django.db.models.fields import DateField


class UserCal(models.Model):
    """UserCal Model
    Fields:
    
    """
    movie_tv= models.ForeignKey("Movie_Tv", on_delete=models.CASCADE)
    all_day = models.BooleanField()
    start = DateField()
    end = DateField()


    