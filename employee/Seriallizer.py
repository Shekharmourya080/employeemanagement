from rest_framework import serializers
from designation.Seriallizer import DesignationSerializer
from department.Seriallizer import DepartmentSerializer


from employee.models import Employee,EmployeeAdd


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
