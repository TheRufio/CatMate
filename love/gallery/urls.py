from django.urls import path
from .views import GalleryView, HomeView
app_name = 'gallery'
urlpatterns = [
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('home/', HomeView.as_view(), name='home')
]