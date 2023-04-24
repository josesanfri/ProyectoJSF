# Django imports
from django.utils.translation import gettext as _

# Third party imports
from django_filters import FilterSet

# Local imports
from applications.base.reserve.models import Reserve

class ReserveFilter(FilterSet):
    class Meta:
        model = Reserve
        fields = ['id', 'status']
        