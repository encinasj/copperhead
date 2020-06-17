from django.db import models
from django.contrib.auth.models import User

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

class MicroBusiness(models.Model):
    #models micro businerss
    name =  models.CharField(max_length=50)
   # img =   models.ImageField(upload_to='inventory/mb')
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'MicroBusiness'
        verbose_name_plural = 'MicroBusinesses'

    def __str__(self):
        return self.name

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
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.name

class Articles(models.Model):
    #models article
    Nuevo = 'Nuevo'
    Semi_nuevo = 'Semi_nuevo'
    Usado = 'Usado'
    Otros = 'Otros'
    STATE_ACTUAL = (
        (Nuevo, 'Nuevo'),
        (Semi_nuevo,'Semi_nuevo'),
        (Usado,'Usado'),
        (Otros,'Otros')
    )
    name = models.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField(null=True)
    fk_brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    fk_category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE) 
    coust_buy = models.DecimalField(max_digits=10, decimal_places=2)
    fk_supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE)
    userful_life = models.DateField()
    actual_state = models.CharField(max_length=12, choices=STATE_ACTUAL)
    date_check = models.DateField()
    location = models.CharField(max_length=50)
    img = models.ImageField(upload_to='articles', null=True, blank=True)
    description = models.TextField(blank=True)
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name
