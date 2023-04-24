# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Local imports
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (_('Account info'), {'fields': ('email', 'password', 'type_user')}),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'created', 'updated')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', ),
        }),
    )
    
    readonly_fields = ( 'created', 'updated')
    list_display = ('id', 'email', 'is_staff', 'type_user', 'created')
    list_display_links = ('id', 'email')
    list_filter = ('is_staff', 'type_user', 'groups')
    search_fields = ['id', 'email__trigram_word_similar']
    ordering = ('-created',)

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('email',)
        return self.readonly_fields
    
admin.site.register(User, CustomUserAdmin)
