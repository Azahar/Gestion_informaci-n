from django.contrib import admin

# Register your models here.
from models import Tlaboratorio, Tmedicamento, Tpantalla, Trol, Tpermiso, Tusuario
from django.contrib import admin

class adminTlaboratorio (admin.ModelAdmin):
	list_display = ("id_laboratorio","nombre_laboratorio")
	##list_filter = ("id_laboratorio", "nombre_laboratorio")
    ##ordering = ('id_laboratorio')
    ##search_fields = ("id_laboratorio")

class adminTmedicamento (admin.ModelAdmin):
	list_display = ("id_medicamento","nombre_medicamento","cantidad_disponible","_laboratorio")

	def _laboratorio(self, obj):
		return obj.laboratorio.id_laboratorio


##class adminTpantalla(admin.ModelAdmin):
##	list_display = ("pantalla")

##class adminTrol (admin.ModelAdmin):
##	list_display = ("rolName","roldes","admin")

##class adminTpermiso(admin.ModelAdmin):
##	list_display = ('rolname','pantalla',"acceso","modificacion")

class adminTusuario (admin.ModelAdmin):
	list_display = ("nombre","password")

	
admin.site.register(Tlaboratorio, adminTlaboratorio)
admin.site.register(Tmedicamento, adminTmedicamento)
admin.site.register(Tpantalla)
admin.site.register(Trol)
admin.site.register(Tpermiso)
admin.site.register(Tusuario, adminTusuario)
