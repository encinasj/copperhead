#Django
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
#models
from .models import Articles, Category, MicroBusiness
#forms
from .forms import ArticlesForm,CategoryForm,MicroBussinesForm

def FeedView(request):
    #list all articles on dashboard
    article = Articles.objects.all()
    context = {
    'article': article
    }
    return render (request, 'inventory/feed.html',context)

def save_all(request,form,template_name):
    #function save articles
    data = dict()
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
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

def create_article(request):
    #function add articles
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
    else:
        form = ArticlesForm()
    return save_all(request,form,'inventory/create_article.html')

def update_article(request, id):
    #fucntion update article
	articles = get_object_or_404(Articles,id=id)
	if request.method == 'POST':
		form = ArticlesForm(request.POST,instance=articles)
	else:
		form = ArticlesForm(instance=articles)
	return save_all(request,form,'inventory/update_article.html')

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
def CategoryView(request):
    #list all category
    category = Category.objects.all()
    microbusiness = MicroBusiness.objects.all()
    context = {
    'category': category,
    'microbusiness': microbusiness
    }
    return render (request, 'inventory/category.html',context)

def save_utilities(request,form,template_name):
    #function save category
    data = dict()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            category = Category.objects.all()
            data['feedc'] = render_to_string('inventory/category_list.html',{'category':category})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

def create_category(request):
    #function add category
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    else:
        form = CategoryForm()
    return save_utilities(request,form,'inventory/category_create.html')

def delete_category(request, id):
    #function delete category
	category = get_object_or_404(Category,id=id)
	data = dict()
	if request.method == 'POST':
		category.delete()
		data['form_is_valid'] = True  #This is just to play along with the existing code
		category = Category.objects.all()
		data['feedc'] = render_to_string('inventory/category_list.html',{'category':category})
	else:
		context = {'category':category}
		data['html_form'] = render_to_string('inventory/category_delete.html',context,request=request)
	return JsonResponse(data)
#====================================================================================================
def save_mb(request,form,template_name):
    #function save category
    data = dict()
    if request.method == 'POST':
        form = MicroBussinesForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            microbusiness = MicroBusiness.objects.all()
            data['feedc'] = render_to_string('inventory/microbusiness_list.html',{'microbusiness':microbusiness})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

def create_microbusiness(request):
    #function create microbusiness
    if request.method == 'POST':
        form = MicroBussinesForm(request.POST)
    else:
        form = MicroBussinesForm()
    return save_mb(request,form,'inventory/create_microbusiness.html')

def delete_microbusiness(request, id):
    #function delete category
	microbusiness = get_object_or_404(MicroBusiness,id=id)
	data = dict()
	if request.method == 'POST':
		microbusiness.delete()
		data['form_is_valid'] = True  #This is just to play along with the existing code
		microbusiness = MicroBusiness.objects.all()
		data['feedc'] = render_to_string('inventory/microbusiness_list.html',{'microbusiness':microbusiness})
	else:
		context = {'microbusiness':microbusiness}
		data['html_form'] = render_to_string('inventory/delete_microbusiness.html',context,request=request)
	return JsonResponse(data)
#====================================================================================================    
def Location(request):
    template_name = 'inventory/location.html'
    return render (request, template_name)

def Report(request):
    template_name = 'base.html'
    return render (request, template_name)

def Configuration(request):
    template_name = 'base.html'
    return render (request, template_name)

def Login(request):
    template_name = 'users/login.html'
    return render (request, template_name)