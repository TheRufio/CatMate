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

    def __str__(self):
        return self.user.username

class ChatProfile(models.Model):
    chat = models.OneToOneField('main.Chat', on_delete=models.CASCADE)
    coins = models.IntegerField()
    max_coins = models.IntegerField()

    def __str__(self):
        return f'{self.chat.name} | profile'

class Chat(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    special_type = models.CharField(
        max_length=6,
        choices=Specials.choices
    )

    def __str__(self):
        return f'{self.name} | chat'

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

    def __str__(self):
        return f'{self.chat.name} | member'

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
        related_name='inventories'
    )
    item = models.ForeignKey(
        'marketplace.Item',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(default=1)

class Achievement(models.Model):
    chat_profile = models.ManyToManyField(
        'main.ChatProfile',
        related_name='achievements'
    )
    name = models.CharField(max_length=80)
    description = models.TextField()
    special_type = models.CharField(
        max_length=6,
        choices=Specials.choices
    )