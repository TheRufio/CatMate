from django.db import models
from main.models import Specials, ChatProfile, Inventory

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

class Currency(models.TextChoices):
    LOVE_COIN = 'love coin', 'Love coin'
    FRIEND_COIN = 'friend coin', 'Friend coin'
    ANY_COIN = 'any coin', 'Any coin'

class ListingStatus(models.TextChoices):
    ACTIVE = 'active', 'Active'
    SOLD = 'sold', 'Sold'
    CANCELLED = 'cancelled', 'Cancelled'

class OrderStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    PAID = 'paid', 'Paid'
    FAILED = 'failed', 'Failed'
    REFUNDED = 'refunded', 'Refunded'

class LedgerReason(models.TextChoices):
    BUY = 'buy', 'Buy'
    SELL = 'sell', 'Sell'

class Item(models.Model):
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=30, choices=ItemType.choices)
    rarity = models.CharField(max_length=12, choices=Rarity.choices)
    price = models.IntegerField()
    special_type = models.CharField(max_length=6, choices=Specials.choices)
    is_tradeable = models.BooleanField(default=True)
    release_at = models.DateField(auto_now_add=True)

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

class Listing(models.Model):
    sellers = models.ForeignKey(
        ChatProfile,
        on_delete=models.CASCADE
    )
    inventory_item = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)
    currency = models.CharField(max_length=11, choices=Currency.choices)
    status = models.CharField(max_length=9, choices=ListingStatus.choices)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
class Order(models.Model):
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE
    )
    buyers = models.ForeignKey(
        ChatProfile,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)
    price_each_cached = models.IntegerField()
    total = models.IntegerField()
    status = models.CharField(choices=OrderStatus.choices)

class Ledger(models.Model):
    from_profile = models.ForeignKey(
        ChatProfile,
        on_delete=models.CASCADE
    )
    from_profile = models.ForeignKey(
        ChatProfile,
        on_delete=models.CASCADE
    )
    amount = models.IntegerField()
    currency = models.CharField(max_length=11, choices=Currency.choices)
    reason = models.CharField(max_length=4, choices=LedgerReason.choices)