from django.urls import path, include
from rest_framework import routers

from api.product.views import ProductTypeViewSet
from api.product.views.product import ProductViewSet

router = routers.SimpleRouter()

router.register(r'type', ProductTypeViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]

