from django.contrib import admin
from shop.models import Branch, Plant
# Register your models here.

class PlantModelAdmin(admin.ModelAdmin):
    list_display = ['branch', 'plantName','code','price','inventory','url','hot']
    list_display_links = ['branch']
    list_filter = ['branch', 'plantName','code','price']
    search_fields = ['plantName']
    list_editable = ['plantName','code','price','inventory','url','hot']
    
    class Meta:
        model = Plant

admin.site.register(Branch)
admin.site.register(Plant, PlantModelAdmin)