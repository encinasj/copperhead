from django.urls import path
from django.contrib.auth.decorators import login_required
from inventory import views

urlpatterns = [
    #CRUD urls Articles and searchbar 
    path('',login_required(views.FeedView), name='feed'),
    path('add',login_required(views.create_article), name='add'),
    path('update/<int:pk>',login_required(views.update_article), name='update'),
    path('details/<int:id>',login_required(views.details_article), name='details'),
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
    
    path('add_pdf',login_required(views.createpdf), name='add_pdf'),
    path('delete_pdf/<int:id>',login_required(views.deletepdf),name='delpdf'),
    
    path('organizations/areas/<int:id>',login_required(views.AreasViews), name='areas_mb'),
    path('organizations/areas/update/<int:id>',login_required(views.update_mb), name='update_mcb'),
    path('organizations',login_required(views.organization), name='corp'),
    
    path('addartic', login_required(views.addarticles), name='addarticle'),
    path('delete_artics/<int:id>', login_required(views.deleteartic), name='deleteartics'),
    #End urls microbusiness

    #CRUD urls comments
    path('add_comment',login_required(views.createcomment), name='add_comment'),
    path('comments/update_comment/<int:id>',login_required(views.updatecomment), name='update_comm'),
    path('comments/del_comment/<int:id>', login_required(views.deletecomment), name='delcomment'),

    #CRD urls brand
    path('add_b',login_required(views.createbrand), name='add_b'),
    path('delete_b/<int:id>',login_required(views.deletebrand), name='delete_b'),
    #End urls brand

    #CRUD supplier
    path('supplier',login_required(views.supplier), name='feed_s'),
    path('add_s',login_required(views.createsupplier), name='add-s'),
    path('details_s/<int:id>',login_required(views.details_suppliers), name='details_s'),
    path('update_s/<int:pk>', login_required(views.updatesupplier), name='update_s'),
    path('delete_s/<int:id>',login_required(views.deletesupplier), name='delete_s'),

    #charts and reports
    path('reports/',login_required(views.chart_reports), name='reports'),
    path('pdf/',login_required(views.write_pdf_view), name='pdf'),
]
