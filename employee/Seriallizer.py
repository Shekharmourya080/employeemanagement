from rest_framework import serializers
from department.Seriallizer import DepartmentSerializer, DepartmentDtoSerializer
from designation.Seriallizer import DesignationSerializer, DesignationDtoSerializer
from employee.models import Employee, EmployeeAdd


class EmployeDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    middleName = serializers.CharField()
    salary = serializers.DecimalField(max_digits=19,decimal_places=6)
    dateOfJoining = serializers.DateField()
    department = DepartmentDtoSerializer()
    designation = DesignationDtoSerializer()





class EmployeeSerializer(serializers.ModelSerializer):
    desId = DesignationSerializer()
    deptId = DepartmentSerializer()
    class Meta:
        model = Employee
        fields = ('firstName', 'lastName', 'middleName', 'dob','dateOfJoining','deptId','desId','salary',)

class EmployeeAddSerializer(serializers.ModelSerializer):
    empid = EmployeeSerializer ()

    class Meta:
        model = EmployeeAdd
        fields =('EmpState','EmpDistrict','EmpContact','empid')
        read_only_fields = ('id',)
