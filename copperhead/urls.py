
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include(('inventory.urls', 'inventory'), namespace='inv')),
    path('users/',include(('users.urls', 'users'), namespace='users')),
    path('admin/', admin.site.urls),
]
