from django.db import models
from registration.models import CustomUser

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
        # User / Profile
"""



class Interes(models.Model):
    name = models.CharField(max_length=80, unique=True)

class Profile(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )
    avatar = models.ImageField(upload_to='avatars/')
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=6,
        choices=Gender.choices
    )
    interests = models.ManyToManyField(Interes)



"""
       # Communication 
"""



class ChatProfile(models.Model):
    # events
    coins = models.IntegerField()
    max_coins = models.IntegerField()
    # achievements
    # inventory
    # gallery
    # style_item (ChatProfileStyle)

class Chat(models.Model):
    chat_profile = models.OneToOneField(
        ChatProfile, 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    special_type = models.CharField(
        max_length=6,
        choices=Specials.choices
    )

class ChatMember(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    chat_avatar = models.ImageField(upload_to='chat/avatars/')
    chat_username = models.CharField(max_length=60)

class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        ChatMember,
        models.CASCADE
    )
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(blank=True)

class Item(models.Model):
    pass
