# Django imports
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.safestring import mark_safe

# Local imports
from .models import Reserve

# Register your models here.
class ReserveAdmin(admin.ModelAdmin):
    list_display= ['id', 'customer', 'restaurant', 'num_customers', 'confirmed_date', 'confirmed_time', 'status', 'created']
    list_filter = ['status']
    search_fields = ['id']
    list_per_page = 40
    ordering=('-created',)
    
admin.site.register(Reserve, ReserveAdmin)
