from django.db import models
from django.db import models

# Create your models here.
class Employee(models.model):
    eid = models.charField(max_length=20)
