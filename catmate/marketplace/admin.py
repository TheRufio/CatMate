from django.contrib import admin
from .models import Item, ChatProfileStyle, Emotion, MessageStyle, GalleryStyle, Listing, Order, Ledger

admin.site.register((Item, ChatProfileStyle, Emotion, MessageStyle, GalleryStyle, Listing, Order, Ledger))