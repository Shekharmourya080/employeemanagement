from rest_framework import serializers

from designation.models import Designation



class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ('id', 'designationName')