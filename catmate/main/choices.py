from django.db import models

class Specials(models.TextChoices):
    NONE = 'none', 'None'
    FRIEND = 'friend', 'Friend'
    LOVE = 'love', 'Love'

class Gender(models.TextChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'