# Django imports
from django import forms
from django.contrib import admin
from django.forms import ModelForm
from django.contrib.postgres.forms import SplitArrayField

# Local imports
from applications.base.location.models import Address, Zone
from applications.base.profileUser.admin import CustomerProfileInline

# Register your models here.
class ZoneAdminForm(ModelForm):
    assigned_postal_codes = SplitArrayField(forms.CharField(), 12, remove_trailing_nulls=True)
    
    class Meta:
        model = Zone
        fields = '__all__'

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'office',)
    list_filter  = ('id',)
    form = ZoneAdminForm
  
class AddresAdmin(admin.ModelAdmin):

    inlines = [CustomerProfileInline]

    class Meta:
        model = Address

admin.site.register(Zone, ZoneAdmin)
admin.site.register(Address, AddresAdmin)

