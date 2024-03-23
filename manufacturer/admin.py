from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from manufacturer.models import Manufacturer


class ManufacturerResource(resources.ModelResource):
    class Meta:
        model = Manufacturer


class ManufacturerAdmin(ImportExportModelAdmin):
    resource_classes = [ManufacturerResource]


admin.site.register(Manufacturer, ManufacturerAdmin)
