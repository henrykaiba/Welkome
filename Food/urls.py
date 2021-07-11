from django.contrib import admin
from django.urls import path, include
from posts.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('eng/', include('eng.urls')),
    path('chi/', include('chi.urls')),
    path('', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
