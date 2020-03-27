#Django
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
#models
from .models import Articles
#forms
from .forms import ArticlesForm

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
        form = ArticlesForm(request.POST)
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
def Category(request):
    template_name = 'inventory/category.html'
    return render (request, template_name)

def Location(request):
    template_name = 'inventory/location.html'
    return render (request, template_name)

def MicroB(request):
    template_name = 'base.html'
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