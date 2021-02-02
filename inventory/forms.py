#Django
from django.contrib.auth.models import User
from django import forms
#models
from inventory.models import Supplier,MicroBusiness,TypeArticle,Category,Brand,Articles

class SupplierForm(forms.ModelForm):
    #supplier forms
    class Meta():
        model = Supplier
        fields = ('name_company','name_contact','phone_number',
                'cel_phone','address','web','email','comments',)
        labels = {
                'name_company':'','name_contact':'','phone_number':'',
                'cel_phone':'','adress':'','web':'','email':'','comments':'',
        }
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
                'cost_buy','fk_supplier','userful_life','actual_state',
                'date_check','location', 'description','img')
        labels = {
                'name':'','quantity':'',
                'fk_brand':'','model':'','fk_category':'', 
                'cost_buy':'','fk_supplier':'','userful_life':'','actual_state':'',
                'date_check':'','location':'', 'description':'','img':''}