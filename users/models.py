#Django
from django.contrib.auth.models import User
from django.db import models
from inventory.models import MicroBusiness

class Profile(models.Model):
    #Profile model.
    #Proxy models that extends the base data with other information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    microbusiness = models.ForeignKey(MicroBusiness, null=True, on_delete=models.SET_NULL)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return username
        return self.user.username

class Remplacement(models.Model):
    #this model add count remplacement in profile
    remplacement = models.CharField(max_length=12, default=0) 

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __srt__(self):
        #return remplacement
        return self.remplacement
    