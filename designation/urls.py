from django.urls import path,include
from rest_framework.routers import DefaultRouter

from designation import  views

router = DefaultRouter()
router.register('designation', viewset=views.DesignationView)

app_name = 'designation'

urlpatterns = [
    path('',include(router.urls))
]