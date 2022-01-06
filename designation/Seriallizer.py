from rest_framework import serializers

from designation.models import Designation



class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ('id', 'designationName')

class DesignationDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    designationName = serializers.CharField()
