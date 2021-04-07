#Django
import os
from django.utils import timezone
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.staticfiles import finders
from django.views.generic import View,TemplateView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string, get_template
from django.http import JsonResponse,Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
import json
from django.db.models import Sum,FloatField,F,Avg, Count,DecimalField
from qr_code.qrcode.utils import ContactDetail

from django.conf import settings
from xhtml2pdf import pisa

#models
from users.models import Profile
from .models import *
#forms
from .forms import *

@login_required
def FeedView(request):
    #list all articles on dashboard
    #search bar
    search_query = request.GET.get('search','') 
    if search_query:
        article = Articles.objects.filter(Q(name__icontains=search_query) | Q(cost_buy__icontains=search_query) | 
        Q(location__icontains=search_query)
        )
    else:
        article = Articles.objects.all()
    #pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(article, 6)
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

@permission_required('is_superuser')
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

@permission_required('is_superuser')
@login_required
def create_article(request):
    #function add articles
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES) 
    else:
        form = ArticlesForm()
    return save_all(request,form,'inventory/create_article.html')

@permission_required('is_superuser')
@login_required
def update_article(request,pk):
    #fucntion update article
    article = get_object_or_404(Articles,pk=pk)
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES, instance=article)
    else:
	    form = ArticlesForm(instance=article)
    return save_all(request, form, 'inventory/update_article.html')

@login_required
def details_article(request, id):
    #function detail article
    article = get_object_or_404(Articles,id=id)
    data = dict() 
    if request.method == 'POST':
        data['form_is_valid'] = True
        article = Articles.objects.all()
        data['feed'] = render_to_string('inventory/list_feed.html',{'article':article})
    else:
	    context = {'article':article}
	    data['html_form'] = render_to_string('inventory/details.html',context,request=request)
    return JsonResponse(data)

@permission_required('is_superuser')
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
@permission_required('is_superuser')
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

@permission_required('is_superuser')
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

@permission_required('is_superuser')
@login_required
def create_category(request):
    #function add category
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    else:
        form = CategoryForm()
    return save_utilities(request,form,'inventory/category/category_create.html')

@permission_required('is_superuser')
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
@permission_required('is_superuser')    
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

@permission_required('is_superuser')
@login_required
def createbrand(request):
    #this function add brands
    if request.method == 'POST':
       form = BrandForm(request.POST)
    else:
        form = BrandForm()
    return save_brand(request,form,'inventory/category/createbrand.html')

@permission_required('is_superuser')
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
@permission_required('is_superuser')
@login_required
def supplier(request):
    #this function show all supplier 
    supplier = Supplier.objects.all()
    context = {
        'supplier':supplier
    }
    return render(request,'inventory/supplier/all_supplier.html', context)

@permission_required('is_superuser')
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

@permission_required('is_superuser')
@login_required
def createsupplier(request):
    #this function add a new supplier
    if request.method == 'POST':
        form = SupplierForm(request.POST)
    else:
        form = SupplierForm()
    return save_supplier(request,form,'inventory/supplier/createsupplier.html')

@permission_required('is_superuser')
@login_required
def details_suppliers(request, id):
    #function detail suppliers
    supplier = get_object_or_404(Supplier,id=id)
    data = dict() 
    if request.method == 'POST':
        data['form_is_valid'] = True
        supplier = Supplier.objects.all()
    else:
	    context = {'supplier':supplier}
	    data['html_form'] = render_to_string('inventory/supplier/details_suppliers.html',context,request=request)
    return JsonResponse(data)

@permission_required('is_superuser')
@login_required
def updatesupplier(request,pk):
    #fucntion update supplier
    supplier = get_object_or_404(Supplier,pk=pk)
    if request.method == 'POST':
	    form = SupplierForm(request.POST, instance=supplier)
    else:
	    form = SupplierForm(instance=supplier)
    return save_supplier(request, form, 'inventory/supplier/updatesupplier.html')

@permission_required('is_superuser')
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
@permission_required('is_superuser')
def chart_reports(request):
    queryset = Articles.objects.all()
    sumatotal = Articles.objects.only('cost_buy').aggregate(Sum('cost_buy'))

    name = [obj.name for obj in queryset]
    quantity = [int(obj.quantity) for obj in queryset]
    total = float(sumatotal['cost_buy__sum'])

    context = {
            'name': json.dumps(name),
            'quantity': json.dumps(quantity),   
            'total':total,
    }
    return render (request,'inventory/chartsandreports/reports.html', context)
#====================================Pdf generator===============================================================
def write_pdf_view(request, *args, **kwargs):
    data = Articles.objects.all()
    suma_total = Articles.objects.aggregate(Sum('cost_buy'))

    total = float(suma_total['cost_buy__sum']) 
    template = get_template('inventory/chartsandreports/PdfsReports.html')
    context = {
        'data': data,
        'total':total,
    }
    html = template.render(context)
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
#==================================organization========================================organization
@permission_required('is_superuser')
@login_required
def organization(request):
    #function save organization or area
    microbusiness = MicroBusiness.objects.all()
    context = {
        'microbusiness': microbusiness,
    }
    return render (request, 'inventory/organization/organization.html', context)

@permission_required('is_superuser')
@login_required
def save_mb(request,form,template_name):
    #function save organization or area
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

@permission_required('is_superuser')
@login_required
def create_microbusiness(request):
    #function create organization or area
    if request.method == 'POST':
        form = MicroBussinesForm(request.POST, request.FILES)
    else:   
        form = MicroBussinesForm()
    return save_mb(request,form,'inventory/category/create_microbusiness.html')

@permission_required('is_superuser')
@login_required
def update_mb(request, id):
    #this function update name of microbusiness area
    microbusiness = get_object_or_404(MicroBusiness, id=id)
    if request.method == 'POST':
        form = MicroBussinesForm(request.POST or None, instance=microbusiness)
    else:
	    form = MicroBussinesForm(instance=microbusiness)
    return save_mb(request, form, 'inventory/organization/update_area.html')

@permission_required('is_superuser')
@login_required
def delete_microbusiness(request, id):
    #function delete organization or area
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
    
@permission_required('is_superuser')
@login_required
def AreasViews(request, id):
    pdfdoc = DocumentsPdf.objects.all()
    allcomment = AllComment.objects.all()
    articlein = AllArticles.objects.all()
    usersin = Profile.objects.all()
    try:
        data = MicroBusiness.objects.get(id = id)
    except MicroBusiness.DoesNotExist:
        raise Http404('Data does not exist')
    context ={
        'pdfdoc':pdfdoc,
        'allcomment':allcomment,
        'articlein':articlein,
        'usersin':usersin,
        'data':data,
    }
    return render(request,'inventory/organization/Areas.html',context)
#=====================================PDF========================================================PDF
@permission_required('is_superuser')
@login_required
def save_pdf(request,form,template_name):
    #function save documents
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            pdfdoc = DocumentsPdf.objects.all()
            data['areas_mb'] = render_to_string('inventory/organization/all_documents.html',{'pdfdoc':pdfdoc})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@permission_required('is_superuser')
@login_required
def createpdf(request):
    #this function add document 
    if request.method == 'POST':
        form = DocumentPdfForm(request.POST, request.FILES)
    else:
        form = DocumentPdfForm()
    return save_pdf(request,form,'inventory/organization/upload.html')

@permission_required('is_superuser')
@login_required
def deletepdf(request, id):
    #function delete document
	pdfdoc = get_object_or_404(DocumentsPdf,id=id)
	data = dict()
	if request.method == 'POST':
		pdfdoc.delete()
		data['form_is_valid'] = True  #This is just to play along with the existing code
		pdfdoc = DocumentsPdf.objects.all()
		data['areas_mb'] = render_to_string('inventory/organization/all_documents.html',{'pdfdoc':pdfdoc})
	else:
		context = {'pdfdoc':pdfdoc}
		data['html_form'] = render_to_string('inventory/organization/DeletePdf.html',context,request=request)
	return JsonResponse(data)  
#=====================================Comments========================================================Comments
@permission_required('is_superuser')
@login_required
def save_comments(request,form,template_name):
    #this function save all comments per area in organization
    pass
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            allcomment = AllComment.objects.all()
            data['area_mb'] = render_to_string('inventory/organization/all_comments.html',{'allcomment':allcomment})
        else:
            data['form_is_valid'] = False
    context = {
        'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@permission_required('is_superuser')
@login_required
def createcomment(request):
    if request.method == 'POST':
        form = AllCommentForm(request.POST or None)
    else:
        form = AllCommentForm()
    return save_comments(request,form,'inventory/organization/createcomment.html')

@permission_required('is_superuser')
@login_required
def details_comments(request, id):
    #function detail suppliers
    allcomment = get_object_or_404(AllComment,id=id)
    data = dict() 
    if request.method == 'POST':
        data['form_is_valid'] = True
        allcomment = AllComment.objects.all()
    else:
	    context = {'allcomment':allcomment}
	    data['html_form'] = render_to_string('inventory/organization/details_comments.html',context,request=request)
    return JsonResponse(data)

@permission_required('is_superuser')
@login_required
def updatecomment(request, id):
    #fucntion update comment
    allcomment = get_object_or_404(AllComment, id=id)
    if request.method == 'POST':
	    form = AllCommentForm(request.POST or None, instance=allcomment)
    else:
	    form = AllCommentForm(instance=allcomment)
    return save_comments(request, form, 'inventory/organization/update_comment.html')

@permission_required('is_superuser')
@login_required
def deletecomment(request, id):
    #this function delete comments
    allcomment = get_object_or_404(AllComment, id=id)
    data =dict()
    if request.method == 'POST':
        allcomment.delete()
        data['form_is_valid'] = True  #This is just to play along with the existing code
        allcomment = AllComment.objects.all()
        data['areas_mb'] = render_to_string('inventory/organization/all_documents.html', {'allcomment':allcomment})
    else:
        context = {'allcomment':allcomment}
        data['html_form'] = render_to_string('inventory/organization/delete_comment.html',context,request=request)
    return JsonResponse(data)    

#=====================================Articles assigned========================================================Articles Assigned
@permission_required('is_superuser')
@login_required
def save_artic(request,form,template_name):
    #this function save all articles per area in organization
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            articlein = AllArticles.objects.all()
            data['area_mb'] = render_to_string('inventory/organization/all_artic.html',{'articlein':articlein})
        else:
            data['form_is_valid'] = False
    context = {
        'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@permission_required('is_superuser')
@login_required
def addarticles(request):
    if request.method == 'POST':
        form = ArticlesAsignedForm(request.POST or None)
    else:
        form = ArticlesAsignedForm()
    return save_artic(request,form,'inventory/organization/addarticle.html')

@permission_required('is_superuser')
@login_required
def deleteartic(request, id):
    #this function delete articles
    articlein = get_object_or_404(AllArticles, id=id)
    data =dict()
    if request.method == 'POST':
        articlein.delete()
        data['form_is_valid'] = True  #This is just to play along with the existing code
        articlein = AllArticles.objects.all()
        data['areas_mb'] = render_to_string('inventory/organization/all_artic.html', {'articlein':articlein})
    else:
        context = {'articlein':articlein}
        data['html_form'] = render_to_string('inventory/organization/delete_artics.html',context,request=request)
    return JsonResponse(data)    