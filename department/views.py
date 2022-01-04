from rest_framework import viewsets,mixins,status
from department.models import Department
from department.Seriallizer import DepartmentSerializer



class DepartmentView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_queryset(self):
        queryset = Department.objects.all().filter()
        return queryset

# Create your views here.
