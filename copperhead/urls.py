
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include(('inventory.urls', 'inventory'), namespace='inv')),
    path('admin/', admin.site.urls),
]
