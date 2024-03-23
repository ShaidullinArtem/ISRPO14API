from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.product.serializers import ProductTypeSerializer
from product.models import ProductType


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = (AllowAny, )
