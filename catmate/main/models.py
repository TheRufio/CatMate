from django.db import models

"""
        # Choices #
"""

class Specials(models.TextChoices):
    NONE = 'none', 'None'
    FRIEND = 'friend', 'Friend'
    Love = 'love', 'Love'

class Gender(models.TextChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'



"""
        # User / Profile #
"""

class Interes(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Profile(models.Model):
    gender = models.CharField(
        max_length=6,
        choices=Gender.choices
    )
    interests = models.ManyToManyField(Interes)





"""
       # Communication #
"""

class Chat(models.Model):
    is_special = models.CharField(
        max_length=6,
        choices=Specials.choices
    )

