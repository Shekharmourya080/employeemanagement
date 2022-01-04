from rest_framework import viewsets,mixins,status
from designation.models import Designation
from designation.Seriallizer import DesignationSerializer



class DesignationView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = DesignationSerializer
    queryset = Designation.objects.all()

    def get_queryset(self):
        queryset = Designation.objects.all()
        return queryset

# Create your views here.
