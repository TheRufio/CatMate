from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls', namespace='registration')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('', include('main.urls', namespace='main'))
]
