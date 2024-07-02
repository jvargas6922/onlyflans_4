from django.db import models

# Create your models here.
class Flan(models.Model):
    name = models.CharField(max_length=60, null=False)
    
    def __str__(self):
        return self.name,


class Postre(models.Model):
    name = models.CharField(max_length=60, null=False,default='name_default')
    color = models.CharField(max_length=20, null=False,default='color_default')
    
    def __str__(self):
        return self.name
    
    
    
    
    
# Campos de texto
#   CharField, TextField
# Campos de números
#   IntegerField, DecimalField, FloatField
# Campos de fecha y hora
#   DateTimeField, DateField, TimeField
# Campos booleanos
#   BooleanField
# Campos Relacionales
#   ForeignKey, OneToOneField, ManyToManyField
# Campos de archivos
#   FileField, ImageField
# Campos de selección
#   ChoiceField
# otros campos
#   EmailField, URLField, UUIDField,
# atributo null= False para que el campo no sea nulo y 
# atributo default para definir un valor por defecto
# atributo unique para que el campo sea único
# atributo primary_key para definir una clave primaria
