from rest_framework import viewsets,mixins,status
from rest_framework.decorators import action
from rest_framework.response import  Response
from department.models import Department
from department.Seriallizer import DepartmentSerializer,DepartmentDtoSerializer
from department.Dto import DepartmentDto



class DepartmentView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_queryset(self):
        queryset = Department.objects.all().filter()
        return queryset

    @action(methods=['GET'], detail=False, url_path='searchDept')
    def get_DepartmentDto(self, request):
        allData = Department.objects.all()
        deptlist = []
        for data in allData:
            deptlist.append(DepartmentDto(data))
        serializer = DepartmentDtoSerializer(deptlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
