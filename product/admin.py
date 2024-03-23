from django.contrib import admin

from product.models import *

admin.site.register(ProductType)
admin.site.register(Product)