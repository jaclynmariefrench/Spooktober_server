from django.db import models

class Waitlist(models.Model):
    """Movie Waitlist"""
    movie_tv = models.ForeignKey("Movie_Tv", on_delete=models.CASCADE)
    spooktober_user = models.ForeignKey("SpooktoberUser", on_delete=models.CASCADE)