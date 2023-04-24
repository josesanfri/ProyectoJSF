from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Local imports
from .models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'created']
    list_filter = ['name']
    search_fields = ['id']
    list_per_page = 40
    ordering=('-created',)
    
admin.site.register(Menu, MenuAdmin)