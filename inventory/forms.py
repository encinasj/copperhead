#Django
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, Textarea
#models
from inventory.models import Supplier,MicroBusiness,TypeArticle,Category,Brand,Articles,DocumentsPdf,AllComment

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
        fields = ('name','img',)


class AllCommentForm(forms.ModelForm):
    class Meta():
        model = AllComment
        fields = ('comment','microbusiness',)


class DocumentPdfForm(forms.ModelForm):
    #Documents pdf
    class Meta():
        model = DocumentsPdf
        fields = ('document','microbusiness',)

"""     def __init__(self, *args, **kwargs):
        super(DocumentPdfForm,self).__init__(*args, **kwargs)
        self.queryset = DocumentsPdf.objects.all() """

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
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
            }
        labels = {
                'name':'','quantity':'',
                'fk_brand':'','model':'','fk_category':'', 
                'cost_buy':'','fk_supplier':'','userful_life':'','actual_state':'',
                'date_check':'','location':'', 'description':'','img':''}
 