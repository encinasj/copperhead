from django.urls import path
from inventory import views

urlpatterns = [
    #CRUD urls Articles
    path('', views.FeedView, name='feed'),
    path('add', views.create_article, name='add'),
    path('update/<int:id>', views.update_article, name='update'),
    path('delete/<int:id>', views.delete_article, name='delete'),
    #End urls articles
    
    #CRD urls Category
    path('Utilities/',views.CategoryView, name='feedc'),
    path('add_c',views.create_category, name='add_c'),
    path('delete_c/<int:id>', views.delete_category, name='delete_c'),
    #End urls Category

    #CRD urls microbusiness
    path('add_m',views.create_microbusiness, name='add_m'),
    path('delete_m/<int:id>', views.delete_microbusiness, name='delete_m'),
    #End urls microbusiness

    path(
        route='location',
        view=views.Location,
        name='location'),
    path(
        route='Login',
        view=views.Login,
        name='login'),
]
