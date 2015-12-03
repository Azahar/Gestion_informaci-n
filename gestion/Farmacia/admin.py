from django.contrib import admin

# Register your models here.
from models import Tlaboratorio, Tmedicamento, Tpantalla, Trol, Tpermiso, Tusuario
from django.contrib import admin

admin.site.register(Tlaboratorio)
admin.site.register(Tmedicamento)
admin.site.register(Tpantalla)
admin.site.register(Trol)
admin.site.register(Tpermiso)
admin.site.register(Tusuario)
