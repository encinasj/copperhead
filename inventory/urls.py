from django.urls import path
from django.contrib.auth.decorators import login_required 
from inventory import views

urlpatterns = [
    #CRUD urls Articles and searchbar 
    path('',login_required(views.FeedView), name='feed'),
    path('add',login_required(views.create_article), name='add'),
    path('update/<int:pk>',login_required(views.update_article), name='update'),
    path('delete/<int:id>',login_required(views.delete_article), name='delete'),
    #End urls Articles
    
    #CRD urls Category
    path('Utilities/',login_required(views.CategoryView), name='feedc'),
    path('add_c',login_required(views.create_category), name='add_c'),
    path('delete_c/<int:id>',login_required(views.delete_category), name='delete_c'),
    #End urls Category

    #CRD urls microbusiness
    path('add_m',login_required(views.create_microbusiness), name='add_m'),
    path('delete_m/<int:id>',login_required(views.delete_microbusiness), name='delete_m'),
    #End urls microbusiness

    #CRD urls brand
    path('add_b',login_required(views.createbrand), name='add_b'),
    path('delete_b/<int:id>',login_required(views.deletebrand), name='delete_b'),
    #End urls brand

    #CRUD supplier
    path('supplier',login_required(views.supplier), name='feed_s'),
    path('add_s',login_required(views.createsupplier), name='add-s'),
    path('update_s/<int:pk>', login_required(views.updatesupplier), name='update_s'),
    path('delete_s/<int:id>',login_required(views.deletesupplier), name='delete_s'),

]
