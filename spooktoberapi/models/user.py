from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    """User Model
    Args:

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    user_calendar = models.ForeignKey("Calendar", on_delete=models.CASCADE)
