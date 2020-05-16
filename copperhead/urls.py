#Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include(('inventory.urls'))),
    path('users/',include(('users.urls', 'users'), namespace='users')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
