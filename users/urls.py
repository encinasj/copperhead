#Django
from django.urls import path
from django.views.generic import TemplateView
from users import views

urlpatterns = [
    path(
        route='login/',
        view=views.login_views,
        name='login',
    ),
    path(
        route='logout/',
        view=views.logout_views,
        name='logout',
    )
]
