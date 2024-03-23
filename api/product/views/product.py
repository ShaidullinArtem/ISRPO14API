from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.product.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        params = self.request.params

        search = params.get('search')
        manufacturer_id = params.get('manufacturer_id')

        if search:
            self.queryset = self.queryset.filter(name__icontains=search)

        if manufacturer_id:
            self.queryset = self.queryset.filter(manufacturer_id=manufacturer_id)

        return self.queryset
