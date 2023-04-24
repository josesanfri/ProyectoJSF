# Django imports
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Local imports
from .models import Plate

# Register your models here.
class PlateAdmin(admin.ModelAdmin):
    list_display= ['id', 'type_plate', 'name', 'price', 'created']
    list_filter = ['type_plate']
    search_fields = ['id']
    list_per_page = 40
    ordering=('-created',)
    
admin.site.register(Plate, PlateAdmin)
