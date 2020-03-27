from django.urls import path
from inventory import views

urlpatterns = [
    #CRUD Articles
    path('', views.FeedView, name='feed'),
    path('add', views.create_article, name='add'),
    path('update/<int:id>', views.update_article, name='update'),
    path('delete/<int:id>', views.delete_article, name='delete'),
    #End urls articles
   path(
        route='Category',
        view=views.Category,
        name='category'),
    path(
        route='location',
        view=views.Location,
        name='location'),
    path(
        route='Login',
        view=views.Login,
        name='login'),
]
