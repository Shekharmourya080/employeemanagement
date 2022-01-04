from django.urls import path,include
from rest_framework.routers import DefaultRouter

from employee import  views

router = DefaultRouter()
router.register('', viewset=views.EmployeeView)
router.register('EmployeeAdd',viewset=views.EmployeeAddView)

app_name = 'employee'

urlpatterns = [
    path('',include(router.urls))
]