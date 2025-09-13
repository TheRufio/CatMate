from django.db import models

class Gallery(models.Model):
    chat_profile = models.ForeignKey(
        'main.ChatProfile',
        on_delete=models.CASCADE,
        related_name='galleries'
    )
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Memory(models.Model):
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='gallery/images/')
    caption = models.CharField(max_length=255)
    added_by = models.ForeignKey(
        'main.ChatMember',
        on_delete=models.CASCADE
    )
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)