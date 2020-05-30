#Django
from django.contrib.auth.decorators import login_required 
from django.views.generic import View,TemplateView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
import json
#models
from .models import Articles,Category,MicroBusiness,Brand,Supplier
#forms
from .forms import ArticlesForm,CategoryForm,MicroBussinesForm,BrandForm,SupplierForm

@login_required
def FeedView(request):
    #list all articles on dashboard

    #search bar
    search_query = request.GET.get('search','') 
    if search_query:
        article = Articles.objects.filter(Q(name__icontains=search_query) | Q(coust_buy__icontains=search_query) | 
        Q(location__icontains=search_query)
        )
    else:
        article = Articles.objects.all()

    #pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(article, 9)
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)

    context = {
    'article': article,
    }
    return render (request, 'inventory/feed.html',context)

@login_required
def save_all(request,form,template_name):
    #function save articles
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            article = Articles.objects.all()
            data['feed'] = render_to_string('inventory/list_feed.html',{'article':article})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required
def create_article(request):
    #function add articles
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
    else:
        form = ArticlesForm()
    return save_all(request,form,'inventory/create_article.html')

@login_required
def update_article(request,pk):
    #fucntion update article
    article = get_object_or_404(Articles,pk=pk)
    if request.method == 'POST':
	    form = ArticlesForm(request.POST, instance=article)
    else:
	    form = ArticlesForm(instance=article)
    return save_all(request, form, 'inventory/update_article.html')

@login_required
def delete_article(request, id):
    #function delete article
	article = get_object_or_404(Articles,id=id)
	data = dict()
	if request.method == 'POST':
		article.delete()
		data['form_is_valid'] = True  #This is just to play along with the existing code
		article = Articles.objects.all()
		data['feed'] = render_to_string('inventory/list_feed.html',{'article':article})
	else:
		context = {'article':article}
		data['html_form'] = render_to_string('inventory/delete_article.html',context,request=request)
	return JsonResponse(data)
#====================================================================================================
@login_required
def CategoryView(request):
    #list all category
    category = Category.objects.all()
    microbusiness = MicroBusiness.objects.all()
    brand = Brand.objects.all()
    context = {
    'category': category,
    'microbusiness': microbusiness,
    'brand':brand
    }
    return render (request, 'inventory/category/category.html',context)

@login_required
def save_utilities(request,form,template_name):
    #function save category
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            category = Category.objects.all()
            data['feedc'] = render_to_string('inventory/category/category_list.html',{'category':category})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required
def create_category(request):
    #function add category
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    else:
        form = CategoryForm()
    return save_utilities(request,form,'inventory/category/category_create.html')

@login_required
def delete_category(request, id):
    #function delete category
	category = get_object_or_404(Category,id=id)
	data = dict()
	if request.method == 'POST':
		category.delete()
		data['form_is_valid'] = True  #This is just to play along with the existing code
		category = Category.objects.all()
		data['feedc'] = render_to_string('inventory/category/category_list.html',{'category':category})
	else:
		context = {'category':category}
		data['html_form'] = render_to_string('inventory/category/category_delete.html',context,request=request)
	return JsonResponse(data)
#====================================================================================================
@login_required
def save_mb(request,form,template_name):
    #function save category
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            microbusiness = MicroBusiness.objects.all()
            data['feedc'] = render_to_string('inventory/category/microbusiness_list.html',{'microbusiness':microbusiness})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required
def create_microbusiness(request):
    #function create microbusiness
    if request.method == 'POST':
        form = MicroBussinesForm(request.POST)
    else:
        form = MicroBussinesForm()
    return save_mb(request,form,'inventory/category/create_microbusiness.html')

@login_required
def delete_microbusiness(request, id):
    #function delete category
	microbusiness = get_object_or_404(MicroBusiness,id=id)
	data = dict()
	if request.method == 'POST':
		microbusiness.delete()
		data['form_is_valid'] = True  #This is just to play along with the existing code
		microbusiness = MicroBusiness.objects.all()
		data['feedc'] = render_to_string('inventory/category/microbusiness_list.html',{'microbusiness':microbusiness})
	else:
		context = {'microbusiness':microbusiness}
		data['html_form'] = render_to_string('inventory/category/delete_microbusiness.html',context,request=request)
	return JsonResponse(data)
#====================================================================================================    
@login_required
def save_brand(request,form,template_name):
    #function save category
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            brand = Brand.objects.all()
            data['feedc'] = render_to_string('inventory/category/brand_list.html',{'brand':brand})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required
def createbrand(request):
    #this function add brands
    if request.method == 'POST':
       form = BrandForm(request.POST)
    else:
        form = BrandForm()
    return save_brand(request,form,'inventory/category/createbrand.html')

@login_required
def deletebrand(request, id):
    #function delete category
	brand = get_object_or_404(Brand,id=id)
	data = dict()
	if request.method == 'POST':
		brand.delete()
		data['form_is_valid'] = True  #This is just to play along with the existing code
		brand = Brand.objects.all()
		data['feedc'] = render_to_string('inventory/category/brand_list.html',{'brand':brand})
	else:
		context = {'brand':brand}
		data['html_form'] = render_to_string('inventory/category/delete_brand.html',context,request=request)
	return JsonResponse(data)
#====================================================================================================   
@login_required
def supplier(request):
    #this function show all supplier 
    supplier = Supplier.objects.all()
    context = {
        'supplier':supplier
    }
    return render(request,'inventory/supplier/all_supplier.html', context)

@login_required
def save_supplier(request,form,template_name):
    #function save supplier
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            supplier = Supplier.objects.all()
            data['feed_s'] = render_to_string('inventory/supplier/supplier_list.html',{'supplier':supplier})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required
def createsupplier(request):
    #this function add a new supplier
    if request.method == 'POST':
        form = SupplierForm(request.POST)
    else:
        form = SupplierForm()
    return save_supplier(request,form,'inventory/supplier/createsupplier.html')

@login_required
def updatesupplier(request,pk):
    #fucntion update supplier
    supplier = get_object_or_404(Supplier,pk=pk)
    if request.method == 'POST':
	    form = SupplierForm(request.POST, instance=supplier)
    else:
	    form = SupplierForm(instance=supplier)
    return save_supplier(request, form, 'inventory/supplier/updatesupplier.html')

@login_required
def deletesupplier(request, id):
    #function delete supplier
	supplier = get_object_or_404(Supplier,id=id)
	data = dict()
	if request.method == 'POST':
		supplier.delete()
		data['form_is_valid'] = True  #This is just to play along with the existing code
		supplier = Supplier.objects.all()
		data['feed_s'] = render_to_string('inventory/supplier/supplier_list.html',{'supplier':supplier})
	else:
		context = {'supplier':supplier}
		data['html_form'] = render_to_string('inventory/supplier/deletesupplier.html',context,request=request)
	return JsonResponse(data)
#====================================================================================================
def chart_reports(request):
    queryset = Articles.objects.all()
    name = [obj.name for obj in queryset]
    quantity = [int(obj.quantity) for obj in queryset]

    context = {
            'name': json.dumps(name),
            'quantity': json.dumps(quantity),
    }
    return render (request,'inventory/chartsandreports/reports.html', context)
#====================================================================================================