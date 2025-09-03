from django.db import models

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