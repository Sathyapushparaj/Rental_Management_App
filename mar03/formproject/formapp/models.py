from django.db import models



# Create your models here.
from django.db import models


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=30)
    econtact = models.CharField(max_length=15)
    address = models.CharField(max_length=100)


class Meta:
    db_table = "Employee"
