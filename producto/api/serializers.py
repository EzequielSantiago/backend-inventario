from rest_framework import serializers
from producto.models import producto

class productoserializer(serializers.ModelSerializer):
    class Meta:
        model=producto
        fields='__all__'