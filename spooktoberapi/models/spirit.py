from spooktoberapi.models import movie_tv
from django.db import models


class Spirit(models.Model):
    """Spirit Model
    Fields:
    
    """
    label= models.CharField(max_length=150)