from django.contrib import admin

from accountcode.models import Function_master,Object_master

# Register your models here.
@admin.register(Function_master)
class Function_masterAdmin(admin.ModelAdmin):
    list_display = ('lookup', 'function_code', 'function_desc','function_parent_id','function_compcode')
    list_filter = ('function_compcode', 'function_desc')
    search_fields = ('function_compcode', 'function_desc')
    ordering = ('function_compcode', 'function_desc') 


@admin.register(Object_master)
class Object_masterAdmin(admin.ModelAdmin):
    list_display = ('lookup','object_code', 'object_desc', 'object_parent_id','object_compcode')
    list_filter = ('object_desc', 'object_compcode')
    search_fields = ('object_desc', 'object_compcode')
    ordering = ('object_compcode', 'object_desc') 


