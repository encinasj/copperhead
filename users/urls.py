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
        route='',
        view=views.users_register,
        name='l_register'),
    path(
        route='register/',
        view=views.register,
        name='register'),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update_profile'),
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'),
]
