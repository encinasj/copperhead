#Django
from django.contrib import admin
from inventory.models import *

admin.site.register(Supplier)
admin.site.register(MicroBusiness)
admin.site.register(TypeArticle)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Articles)
admin.site.register(AllComment)
admin.site.register(DocumentsPdf)
