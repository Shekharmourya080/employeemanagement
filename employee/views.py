from rest_framework import viewsets,mixins,status
from rest_framework.decorators import action
from rest_framework.response import  Response
from employee.models import Employee,EmployeeAdd
from employee.Seriallizer import EmployeeSerializer,EmployeeAddSerializer,EmployeDtoSerializer,EmployeeAddDtoSerializer
from employee.Dto import EmployeeDto
from employee.Dto import EmployeeAddDto

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class EmployeeView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get_queryset(self):
        queryset = Employee.objects.all()
        return queryset

    @action(methods=['GET'],detail=False,url_path='getAll')
    def get_all_employess(self,request):
        allData = Employee.objects.all()
        empList = []
        for data in allData:
            empList.append(EmployeeDto(data))
        serializer = EmployeDtoSerializer(empList,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(methods=['GET'], detail=False, url_path='EmployeeName')
    def FirstName(self, request):
        firstName = self.request.query_params.get('firstName')
        queryset = Employee.objects.all().filter(firstName__contains=firstName)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='findByDepartment')
    def SearchByDepartment(self, request):
        DepartmentName = self.request.query_params.get('SearchByDepartment')
        queryset = Employee.objects.all().filter(deptId__deptName__contains=DepartmentName)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'],detail= False, url_path='findByDesignation')
    def SearchByDesignation(self, request):
        DesignationName = self.request.query_params.get('SearchByDesignation')
        queryset = Employee.objects.all().filter(desId__designationName__icontains=DesignationName)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)








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

    @action(methods=['GET'],detail=False,url_path='searchByEmpAdd')
    def get_EmployeeAddDto(self,request):
        allData = EmployeeAdd.objects.all()
        Empaddlist = []
        for data in allData:
            Empaddlist.append(EmployeeAddDto(data))
        serializer = EmployeeAddDtoSerializer(Empaddlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


