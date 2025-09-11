from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls', namespace='registration')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('', include('main.urls', namespace='main'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)