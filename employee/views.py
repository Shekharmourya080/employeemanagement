from rest_framework import viewsets,mixins,status
from rest_framework.decorators import action
from rest_framework.response import  Response
from employee.models import Employee,EmployeeAdd
from employee.Seriallizer import EmployeeSerializer,EmployeeAddSerializer




class EmployeeView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get_queryset(self):
        queryset = Employee.objects.all().filter()
        return queryset

    @action(methods=['GET'], detail=False, url_path='EmployeeName')
    def FirstName(self, request):
        firstName = self.request.query_params.get('firstName')
        queryset = Employee.objects.all().filter(firstName__contains=firstName)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class EmployeeAddView(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = EmployeeAddSerializer
    queryset = EmployeeAdd.objects.all()

    def get_queryset(self):
        queryset = EmployeeAdd.objects.all()
        return queryset

    @action(methods=['GET'], detail=False, url_path='searchByEmployeeAdd')
    def EmployeeAdd(self, request):
        EmpState = self.request.query_params.get('EmpState')
        queryset = EmployeeAdd.objects.all().filter(EmpState=EmpState)
        serializer = EmployeeAddSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


