from django.contrib import admin
from .models import UserProfile, ChatProfile, Chat, Message, ChatMember, Interes, Inventory, Achievement

admin.site.register((UserProfile, ChatProfile, Chat, Message, ChatMember, Interes, Inventory, Achievement))