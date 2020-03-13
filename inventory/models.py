from django.db import models
from django.contrib.auth.models import User

#models inventory
class Supplier(models.Model):
    #supplier model.
    name_company =  models.CharField(max_length=60)
    name_contact =  models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    adress = models.CharField(max_length=60)
    cel_phone = models.CharField(max_length=12)
    web = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
    comments = models.TextField(blank=True)
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    delete = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name_company

class MicroBusiness(models.Model):
    #models micro businerss
    name =  models.CharField(max_length=50)
    img =   models.ImageField(upload_to='inventory/mb')
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    delete = models.DateField(auto_now=True)

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
    delete = models.DateField(auto_now=True)

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
    delete = models.DateField(auto_now=True)

    
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
    delete = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.name

class Articles(models.Model):
    #models article
    STATE_ACTUAL = (
        ('N', 'Nuevo'),
        ('S','Semi nuevo'),
        ('U','Usado'),
        ('O','Otros')
    )
    name = models.CharField((""), max_length=50)
    img =   models.ImageField(upload_to='inventory/articles')
    quantity = models.DecimalField(max_digits=4, decimal_places=3)
    fk_brand = models.ManyToManyField(Brand)
    model = models.CharField(max_length=50)
    fk_category = models.ManyToManyField(Category)
    coust_buy = models.DecimalField(max_digits=10, decimal_places=2)
    fk_supplier = models.ManyToManyField(Supplier)
    description = models.TextField(blank=True)
    userful_life = models.DateField()
    actual_state = models.CharField(max_length=1, choices=STATE_ACTUAL)
    date_check = models.DateField()
    fk_user = models.ManyToManyField(User)
    fk_microbusiness = models.ManyToManyField(MicroBusiness)
    location = models.CharField(max_length=50)
    #actions
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    delete = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name
