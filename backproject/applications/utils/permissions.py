# Third party imports
from rest_framework.permissions import BasePermission

# Local imports
from applications.base.user.models import User

class IsCustomerOrAdminUser(BasePermission):
    """
    Allows access only to renter users or admin users.
    """

    def has_permission(self, request, view):
        return (request.user.type_user == User.CUSTOMER or request.user.is_staff)
    
    
class IsObjAuthorOrStaff(BasePermission):
    """
    Allows access only to object author (the user who has created the object) or a staff user.

    This permission is specially suited for UPDATE RETRIEVE & DESTROY views,
    when the object has a Foreign Key to User
    """

    # Works with GET, PUT, DELETE. POST method not allowed
    def has_object_permission(self, request, view, obj):        
        if request.user.is_staff:
            return True

        elif hasattr(obj, 'user'):
            return obj.user == request.user 
        
        elif hasattr(obj, 'customer') and request.user.type_user == User.CUSTOMER:
            return obj.customer == request.user or (request.user in obj.extra_customer.all())
        
        return False  