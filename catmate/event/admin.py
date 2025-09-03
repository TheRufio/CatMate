from django.contrib import admin
from .models import Event, Events, GiftItem

admin.site.register((Event, Events, GiftItem))