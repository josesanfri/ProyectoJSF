# Django imports
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


# Local imports
from applications.base.timestamp.models import Timestamp
from applications.base.restaurant.models import Restaurant


# Create your models here.
class Department(Timestamp):
    restaurant = models.ForeignKey(to=Restaurant, on_delete=CASCADE, null=False, related_name='%(class)s', verbose_name=_('Restaurant'))
    name = models.CharField(_('Department name'), max_length=30, unique=True, null=False)
    dept_phone = models.CharField(_('Department phone'), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Department')
        
class SubDepartment(Timestamp):
    principal_department = models.ForeignKey(to=Department, on_delete=CASCADE, null=False, related_name='principal_department', verbose_name= _('Principal department'))
    secondary_department = models.ForeignKey(to=Department, on_delete=CASCADE, null=False, related_name='sub_department', verbose_name= _('Sub department'))

    def __str__(self):
        return (f'{self.secondary_department} es un departamento de {self.principal_department}')

    class Meta:
        verbose_name =  _('Subdepartment')
        verbose_name_plural = _('Subdepartments')
    