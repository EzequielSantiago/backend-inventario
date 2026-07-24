from rest_framework import viewsets
from producto.models import producto
from producto.api.serializers import productoserializer

class productoviewset(viewsets.ModelViewSet):
    queryset=producto.objects.all()
    serializer_class=productoserializer
    