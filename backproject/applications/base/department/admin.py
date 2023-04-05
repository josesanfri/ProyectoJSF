# Django imports
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.models import LogEntry


# Local imports
from .models import Department, SubDepartment

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'restaurant', 'name', 'dept_phone']

class SubdepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'principal_department', 'secondary_department', 'get_restaurant' ]

    @admin.display(description=_('Restaurant'))
    def get_restaurant(self, obj):
        return obj.principal_department.restaurant

admin.site.register(Department, DepartmentAdmin)
admin.site.register(SubDepartment, SubdepartmentAdmin)

