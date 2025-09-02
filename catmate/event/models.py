from django.db import models
from main.models import ChatProfile
from marketplace.models import Item, Currency

class Events(models.Model):
    members = models.ManyToManyField(ChatProfile)

class Event(models.Model):
    event = models.ForeignKey(
        Events,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=120)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class GiftItem(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )
    award_item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )
    item_quantity = models.IntegerField()
    award_coin = models.IntegerField(blank=True)
    currency = models.CharField(choices=Currency.choices)