from django.contrib import admin
from lookup.models import Lookup,Lookupdet
# Register your models here.


@admin.register(Lookup)
class LookupAdmin(admin.ModelAdmin):
    list_display = ('lookupcode', 'lookname', 'status')
    list_filter = ('lookname', 'status')
    search_fields = ('lookupcode', 'lookname')
    ordering = ('status', 'lookname') 


@admin.register(Lookupdet)
class LookupdetAdmin(admin.ModelAdmin):
    list_display = ('lookup','lookupdetdesc', 'lookupvalue', 'status')
    list_filter = ('lookupdetdesc', 'lookupvalue')
    search_fields = ('lookupdetdesc', 'lookupvalue')
    ordering = ('status', 'lookupdetdesc') 


