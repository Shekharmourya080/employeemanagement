from django.db import models
from designation.models import Designation
from department.models import Department

class Employee(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, db_column='emp_id')
    firstName = models.CharField(max_length=100, db_column='first_name')
    lastName = models.CharField(max_length=100, db_column='last_name')
    middleName = models.CharField(max_length=100, db_column='middle_name', null=True)
    dob = models.DateField()
    salary = models.DecimalField(max_digits=19, decimal_places=6, db_column='Emp_salary')
    dateOfJoining = models.DateField(db_column='date_of_joining')
    deptId = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, db_column='dept_id')
    desId = models.ForeignKey(to=Designation,on_delete=models.CASCADE,null=True,db_column='des_id')

    def __str__(self):
        return self.firstName + ' '+ self.lastName

class EmployeeAdd(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, db_column='EmpAdd_id')
    EmpState = models.CharField(max_length=100,db_column='Employee_State')
    EmpDistrict = models.CharField(max_length=100,db_column='Employee_District')
    EmpContact = models.IntegerField(db_column='Emp_contact')
    empid = models.ForeignKey(to=Employee, on_delete=models.CASCADE, null=True, db_column='Emp_id')

# Create your models here.
