# Django imports
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from applications.base.user.models import User

def customer_user(id):
    """Checks if the user's type is CUSTOMER

    Args:
        id (Integer): user's identifyer

    Raises:
        ValidationError: If the user is not a CUSTOMER
    """
    user = User.objects.get(pk=id)

    if user.type_user != User.CUSTOMER:
      raise ValidationError(_('%(user)s must be a customer') % {'user' : user})

  
def validate_positive_value(value):
    """Validates if the value is positive

    Args:
        value ([num]): A numerical value: integer or float

    Raises:
        ValidationError: Indicates that the number must be positive
    """
    if value < 0:
        raise ValidationError(_('(%(value)s) must be a positive number') % {'value' : value})

