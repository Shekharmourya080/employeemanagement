from django.db import models
class Department(models.Model):
    """Department Table"""
    objects = models.Manager()
    deptName = models.CharField(unique=True, db_column='dept_name',max_length=100)
    deptContactPerson = models.CharField(max_length=100,db_column='dept_contact_person')
# Create your models here.
