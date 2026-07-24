from django.db import models

# Create your models here.
class producto(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.FloatField()
    descripcion=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    