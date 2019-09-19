from django.contrib import admin

from models import Persona
from models import Producto
from models import Compra

# Register your models here.

admin.site.Register(Producto)

admin.site.Register(Persona)

admin.site.Register(Compra)
