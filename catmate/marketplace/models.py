from django.db import models
from main.models import Specials

class ItemType(models.TextChoices):
    EMOTION = 'emotion', 'Emotion'
    MESSAGE = 'message', 'Message'
    PROFILE = 'profile', 'Profile'
    GALLERY = 'gallery', 'Gallery'


class Rarity(models.TextChoices):
    COMMON = "common", "Common"
    UNCOMMON = "uncommon", "Uncommon"
    RARE = "rare", "Rare"
    EPIC = "epic", "Epic"
    LEGENDARY = "legendary", "Legendary"
    MYTHIC = "mythic", "Mythic"
    EXOTIC = "exotic", "Exotic"
    DIVINE = "divine", "Divine"
    CELESTIAL = "celestial", "Celestial"
    UNIQUE = "unique", "Unique"

class Item(models.Model):
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=30, choices=ItemType.choices)
    rarity = models.CharField(max_length=12, choices=Rarity.choices)
    price = models.IntegerField()
    special_type = models.CharField(max_length=6, choices=Specials.choices)
    is_tradeable = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.rarity == Rarity.UNIQUE:
            self.is_tradeable = False
        super().save(*args, **kwargs)

class ChatProfileStyle(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='profile')
    background = models.ImageField(upload_to='items/chat_profile_style/')
    header = models.ImageField(upload_to='items/chat_profile_style/')
    font_style = models.CharField(max_length=50)

class Emotion(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='emotion')
    image = models.ImageField(upload_to='items/emotion/')
   
class MessageStyle(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='message')
    background = models.ImageField(upload_to='items/message_style/')
    border = models.ImageField(upload_to='items/message_style/')
    font_style = models.CharField(max_length=50)

class GalleryStyle(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='items/gallery_style/')
    border = models.ImageField(upload_to='items/gallery_style/')
    font_style = models.CharField(max_length=50)
