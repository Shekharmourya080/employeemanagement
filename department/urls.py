from django.urls import path,include
from rest_framework.routers import DefaultRouter

from department import  views

router = DefaultRouter()
router.register('department', viewset=views.DepartmentView)

app_name = 'depatment'

urlpatterns = [
    path('',include(router.urls))
]