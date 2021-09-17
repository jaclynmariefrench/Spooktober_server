from spooktoberapi.models.spooktober_user import SpooktoberUser
from django.db import models
from spooktoberapi.models.movie_tv import Movie_Tv
from django.db.models.fields import DateTimeField


class UserCal(models.Model):
    """UserCal Model
    Fields:
    
    """
    spooktober_user = models.OneToOneField(SpooktoberUser, on_delete=models.CASCADE)
    movie_tv= models.ForeignKey("Movie_Tv", on_delete=models.CASCADE)
    all_day = models.BooleanField()
    start = DateTimeField()
    end = DateTimeField()

    @property
    def title(self):
        """Grabbing the MovieTv title for calendar"""
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value
    