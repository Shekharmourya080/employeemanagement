from django.db import models


class Designation(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, db_column='Des_id')
    designationName = models.CharField(max_length=100, db_column='Des_name')

# Create your models here.
