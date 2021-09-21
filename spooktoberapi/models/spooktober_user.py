from spooktoberapi.models.movie_tv import Movie_Tv
from django.db import models
from django.contrib.auth.models import User


class SpooktoberUser(models.Model):
    """SpooktoberUser Model
    Args:
        models (OneToOneField): The user information for the gamer
        
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def username(self):
        """username"""
        return self.__title

    @username.setter
    def username(self, value):
        self.__username = value