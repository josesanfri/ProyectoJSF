# Python imports
from datetime import datetime

# Django imports
from django.utils.translation import gettext as _

# Third party imports
from django_filters import filters, FilterSet

# Local imports
from applications.base.restaurant.models import Restaurant

class RestaurantFilter(FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    zone = filters.CharFilter(method='zone_filter')
    address__street = filters.CharFilter(field_name="address__street", lookup_expr='unaccent__trigram_word_similar')
    address__city = filters.CharFilter(field_name="address__city", lookup_expr='unaccent__trigram_word_similar')

    class Meta:
        model = Restaurant
        fields = ['id', 'zone', 'address__street', 'address__city']

    def zone_filter(self, queryset, name, value):
        if value.isdigit():
            return queryset.filter(address__zone = value)

        return queryset.filter(address__zone__name__unaccent__trigram_word_similar = value)
