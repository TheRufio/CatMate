from django.db import models
from .choices import Gender, Specials

class Interes(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(
        'registration.CustomUser',
        on_delete=models.CASCADE,
        related_name='userprofile'
    )
    avatar = models.ImageField(upload_to='avatars/')
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=6,
        choices=Gender.choices
    )
    interests = models.ManyToManyField(Interes)

class ChatProfile(models.Model):
    coins = models.IntegerField()
    max_coins = models.IntegerField()
    
    achievement = models.ForeignKey(
        'Achievement',
        on_delete=models.CASCADE
    )
    events = models.ForeignKey(
        'event.Events',
        on_delete=models.CASCADE
    )

    
    inventory = models.ForeignKey(
        'Inventory',
        on_delete=models.CASCADE
    )
    gallery = models.ForeignKey(
        'gallery.Gallery',
        on_delete=models.CASCADE
    )
    style_item = models.ForeignKey(
        'marketplace.Item',
        on_delete=models.CASCADE,
        related_name='style'
    )

class Chat(models.Model):
    chat_profile = models.OneToOneField(
        ChatProfile, 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
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
        'registration.CustomUser',
        on_delete=models.CASCADE
    )
    chat_avatar = models.ImageField(upload_to='chat/avatars/')
    chat_username = models.CharField(max_length=60)

    class Meta:
        unique_together = ('chat', 'user')

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
    timestamp = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(blank=True, auto_now=True)

class Inventory(models.Model):
    chat_profile = models.ForeignKey(
        ChatProfile,
        on_delete=models.CASCADE,
        related_name='chat_profile_inventory'
    )
    item = models.ForeignKey(
        'marketplace.Item',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(default=1)

class Achievement(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    special_type = models.CharField(
        max_length=6,
        choices=Specials.choices
    )