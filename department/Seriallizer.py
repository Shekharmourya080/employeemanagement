from rest_framework import serializers

from department.models import Department



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('deptName','deptContactPerson')

class DepartmentDtoSerializer(serializers.Serializer):
    deptName = serializers.CharField()
    deptContactPerson = serializers.CharField()
