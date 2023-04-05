# Third party imports
from rest_framework import viewsets

# Local imports
from .serializers import DepartmentSerializer, SubDepartmentSerializer
from .models import Department, SubDepartment

#  Create your viewsets here
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class SubDepartmenteViewSet(viewsets.ModelViewSet):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer