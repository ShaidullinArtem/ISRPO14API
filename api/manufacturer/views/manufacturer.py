from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.manufacturer.serializers import ManufacturerSerializer
from manufacturer.models import Manufacturer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (AllowAny, )
