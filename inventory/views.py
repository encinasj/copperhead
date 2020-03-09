from django.shortcuts import render


def FeedView(request):
    template_name = 'inventory/feed.html'
    return render (request, template_name)

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