from django.urls import path
from inventory import views

urlpatterns = [
    path(
        route='',
        view=views.FeedView,
        name='feed'),
   path(
        route='/Category',
        view=views.Category,
        name='category'),
    path(
        route='/location',
        view=views.Location,
        name='location'),
    path(
        route='/Login',
        view=views.Login,
        name='login'),
]
