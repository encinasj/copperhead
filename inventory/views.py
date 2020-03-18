from django.template.loader import render_to_string
from django.http import JsonResponse

from django.shortcuts import render
from .models import Articles

def FeedView(request):
    #list all articles on dashboard
    article = Articles.objects.all()
    context = {
    'article': article
    }
    template_name = 'inventory/feed.html'
    return render (request, template_name, context)

def save_all(request,form,template_name):
    #function add articles
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            article = Articles.objects.all()
            data['all_list'] = render_to_string('inventory/list_feed.html',{'article':article})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

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