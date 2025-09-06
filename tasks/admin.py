from django.contrib import admin
from.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')   #list las columnnas que se van a mostrar
    search_fields = ('title',) #campos por los que se puede buscar
    list_filter = ('created_at', 'updated_at') #filtros en la barra lateral




#siempre que se agrega una clase se debe registrar en el admin
admin.site.register(Task, TaskAdmin)

