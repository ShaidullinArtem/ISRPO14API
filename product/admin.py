from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from product.models import Product, ProductType


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class ProductAdmin(ImportExportModelAdmin):
    resource_classes = [ProductResource]


admin.site.register(Product, ProductAdmin)


class ProductTypeResource(resources.ModelResource):
    class Meta:
        model = ProductType


class ProductTypeAdmin(ImportExportModelAdmin):
    resource_classes = [ProductTypeResource]


admin.site.register(ProductType, ProductTypeAdmin)
