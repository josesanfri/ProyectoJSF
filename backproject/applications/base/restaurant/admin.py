# Django imports
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

# Local imports
from applications.base.restaurant.models import Restaurant, MediaRestaurant

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Main'), {'fields': ('name_restaurant', 'slug_restaurant')}),
        (_('Basic features'), {
            'fields': ('address', 'square_meters', ),
        }),
        (_('Options'), {'fields': ['is_managed']}),
        (_('CRM features'), {'fields': ('caption_user', 'management_user')}),
        (_('Others'), {'fields': ['description']}),
    )

    readonly_fields = ('created', 'updated')
    list_display = ('id', 'is_managed', 'address', 'created')
    list_display_links = ('id', 'address')
    list_filter = ('is_managed', 'address__zone')
    search_fields = ['id', 'address__street__unaccent__trigram_word_similar', 'address__number']
    search_help_text = _('Insert here Restaurant ID, address')
    ordering = ('-created', 'id',)

class MediaRestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('restaurant','id', 'image', 'is_cover', 'created')
    search_fields = ['id']
    search_help_text = _('Insert here Restaurant ID ')
    ordering = ('-created', 'id', 'restaurant')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(MediaRestaurant, MediaRestaurantAdmin)
