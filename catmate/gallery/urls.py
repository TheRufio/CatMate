from django.urls import path
from .views import GalleryView, AddMemoryView, AddGalleryView
app_name = 'gallery'
urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),
    path('add-memory/', AddMemoryView.as_view(), name='add_memory'),
    path('add-gallery/', AddGalleryView.as_view(), name='add_gallery')
]