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
    ),
    path(
        route='register/',
        view=views.users_register,
        name='l_register'),
]
