from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

#models inventory
class Supplier(models.Model):
    #supplier model.
    name_company =  models.CharField(max_length=60)
    name_contact =  models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    cel_phone = models.CharField(max_length=12)
    address = models.CharField(max_length=60)
    web = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
    comments = models.TextField(blank=True)
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name_company

class TypeArticle(models.Model):
    #models type article
    name = models.CharField(max_length=50)
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'TypeArticle'
        verbose_name_plural = 'TypeArticles'

    def __str__(self):
        return self.name

class Category(models.Model):
    #models category
    name = models.CharField(max_length=50)
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name

class Brand(models.Model):
    #models brand
    name = models.CharField(max_length=50)
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

class Articles(models.Model):
    #models article
    Nuevo = 'Nuevo'
    Semi_nuevo = 'Seminuevo'
    Usado = 'Usado'
    Otros = 'Otros'
    STATE_ACTUAL = (
        (Nuevo, 'Nuevo'),
        (Semi_nuevo,'Seminuevo'),
        (Usado,'Usado'),
        (Otros,'Otros')
    )
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    fk_brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    model = models.CharField(max_length=50)
    fk_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL) 
    cost_buy = models.DecimalField(max_digits=10, decimal_places=2)
    fk_supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    userful_life = models.DateField()
    actual_state = models.CharField(max_length=12, choices=STATE_ACTUAL)
    date_check = models.DateField()
    location = models.CharField(max_length=50)
    img = models.ImageField(upload_to='articles', null=True, blank=True)
    qr = models.ImageField(upload_to='qrcodes', null=True, blank=True, max_length=255)
    total_todo = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    description = models.TextField(max_length=500, blank=True)
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        return (self.cost_buy*self.quantity)
    
    def calculate_amount(self):
        self.total_todo = self.cost_buy * self.quantity

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self, *args, **kwargs):
        return str(self.name)

    def save(self, *args, **kwargs):
        #Create a qr code and save it, generate a png image. 
        qrcode_img = qrcode.make(['Nombre: ',self.name,'Modelo: ',self.model, 'Cantidad: ',self.quantity, 'descripción: ',self.description])
        canvas = Image.new('RGB', (800,800), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code_{self.name,self.model,self.quantity,self.description}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr.save(fname, File(buffer), save=False)
        canvas.close()
        self.calculate_amount()
        super().save(*args, **kwargs)

class MicroBusiness(models.Model):
    #models micro business
    name =  models.CharField(max_length=50, null=False, blank=False)

    #dates
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'MicroBusiness'
        verbose_name_plural = 'MicroBusinesses'

    def __str__(self):
        return str(self.name)

class ImgArea(models.Model):
    img = models.ImageField(upload_to='ImgAreas', null=False, blank=False)
    #dates
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ImgArea'
        verbose_name_plural = 'ImgAreas'

    def __str__(self):
        return str('img') + '-' + str(self.id)

class AllComment(models.Model):
    microbusiness = models.ForeignKey(MicroBusiness, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)

    #dates
    create = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'AllComment'
        verbose_name_plural = 'AllComments' 

    def __str__(self):
        return str(self.comment)

class DocumentsPdf(models.Model):
    microbusiness = models.ForeignKey(MicroBusiness, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents', null=False, blank=False)

    #dates
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'DocumentsPdf'
        verbose_name_plural = 'DocumentsPdfs'

    def __str__(self):
        return str('Document') +'-'+ str(self.create)

class AllArticles(models.Model):
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    microbusiness = models.ForeignKey(MicroBusiness, on_delete=models.CASCADE)

    #adding
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'AllArticle'
        verbose_name_plural = 'AllArticles'

    def __str__(self):
        return str(self.articles)
    
    