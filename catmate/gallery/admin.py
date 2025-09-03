from django.contrib import admin
from .models import Gallery, Memory

admin.site.register((Gallery, Memory))