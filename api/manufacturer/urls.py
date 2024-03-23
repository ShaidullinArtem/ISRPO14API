from django.urls import path, include
from rest_framework import routers

from api.manufacturer.views import ManufacturerViewSet

router = routers.SimpleRouter()

router.register(r'manufacturer', ManufacturerViewSet)

urlpatterns = [
    path('', include(router.urls))
]

