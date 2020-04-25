#Django
from django.contrib.auth.models import User
from django import forms
#models
from inventory.models import Supplier,MicroBusiness,TypeArticle,Category,Brand,Articles

class SupplierForm(forms.Form):
    #supplier forms
    name_company = forms.CharField(min_length=4, max_length=20, required=True)
    name_contact = forms.CharField(min_length=4,max_length=20, required=True)
    phone_number = forms.CharField(min_length=4, max_length=12, required=True)
    adress = forms.CharField(min_length=4,max_length=60, required=False)
    cel_phone = forms.CharField(min_length=4,max_length=12, required=False)
    web = forms.URLField(min_length=4,max_length=200, required=False)
    emial = forms.EmailField(min_length=4,max_length=254, required=False)
    comments = forms.CharField(max_length=250, required=False)

class MicroBussinesForm(forms.ModelForm):
    #Microbusiness Form
     class Meta():
        model = MicroBusiness
        fields = ('name',)

class TypeArticlesForm(forms.Form):
    #Type Article Form
    name_ta = forms.CharField(min_length=4, max_length=50, required=True)

class CategoryForm(forms.ModelForm):
    #Category Form
    class Meta():
        model = Category
        fields = ('name',)

class BrandForm(forms.ModelForm):
    #Brand Form
    class Meta():
        model = Brand
        fields = ('name',)

class ArticlesForm(forms.ModelForm):
    #Article Form
    class Meta():
        model = Articles
        fields = (
                'name','quantity',
                'fk_brand','model','fk_category', 
                'coust_buy','fk_supplier','userful_life','actual_state',
                'date_check','fk_user','fk_microbusiness','location',
                'description')
        labels = {
                'name':'','quantity':'',
                'fk_brand':'','model':'','fk_category':'', 
                'coust_buy':'','fk_supplier':'','userful_life':'','actual_state':'',
                'date_check':'','fk_user':'','fk_microbusiness':'','location':'',
                'description':'',}

