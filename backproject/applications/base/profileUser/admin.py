# Django imports
from django.contrib import admin
from django.forms import ModelForm, Textarea, CharField
from django.utils.translation import gettext_lazy as _

# Local imports
from .models import CustomerProfile, StaffProfile, Address

# Register your models here.  
class AbstractProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Account info'), {'fields': ('user', 'image')}),
        (_('Personal data'), {
            'fields': ('first_name', 'last_name', 'birth_date', 'prefix_phone', 'phone', 'gender', 
            'annotation_gender', 'address' ),
        }),
        (_('Actions'), {'fields': ('created', 'created_by', 'updated', 'updated_by')}),
    )
    
    readonly_fields = ('created', 'created_by', 'updated_by', 'updated')
    list_display = ('__str__', 'user', 'created')
    ordering = ('-created',)
    
    def delete_queryset(self, request, queryset):
        for address in queryset.values('address_id'):
            Address.objects.get(id=address.get('address_id')).delete()
        return super().delete_queryset(request, queryset)

    class Meta:
        abstract = True

# Customer profile
class CustomerProfileForm(ModelForm):
    description = CharField(widget=Textarea, required=False)
    
    class Meta:
        model = CustomerProfile
        fields = '__all__'

@admin.register(CustomerProfile)
class CustomerProfileAdmin(AbstractProfileAdmin):
    form = CustomerProfileForm

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(super(CustomerProfileAdmin, self).get_fieldsets(request, obj))
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(CustomerProfileAdmin, self).get_readonly_fields(request, obj))
        return readonly_fields

    class Meta:
        model = CustomerProfile

# Admin register
reg_models = [StaffProfile]
admin.site.register(reg_models)

# Inlines for other admin pages
class CustomerProfileInline(admin.StackedInline):
    model = CustomerProfile
    