from rest_framework import viewsets,mixins,status
from rest_framework.decorators import action
from rest_framework.response import  Response
from designation.models import Designation
from designation.Seriallizer import DesignationSerializer,DesignationDtoSerializer
from designation.Dto import DesignationDto



class DesignationView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = DesignationSerializer
    queryset = Designation.objects.all()

    def get_queryset(self):
        queryset = Designation.objects.all()
        return queryset

    @action(methods=['GET'], detail=False, url_path='searchDes')
    def get_DesignationDto(self, request):
        allData = Designation.objects.all()
        deslist = []
        for data in allData:
            deslist.append(DesignationDto(data))
        serializer = DesignationDtoSerializer(deslist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
