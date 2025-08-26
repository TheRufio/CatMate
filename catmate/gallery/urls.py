from django.urls import path
from .views import GalleryView, HomeView, LogoutView, ProfileView
app_name = 'gallery'
urlpatterns = [
    path('logout', LogoutView.as_view(), name='logout'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile', ProfileView.as_view(), name='profile')
]