from django.db import models

# Create your models here.
class search(models.Model):
    address= models.CharField(max_length=200, null=True)
    long = models.DecimalField(max_digits=30, decimal_places=1, null=True)
    lat = models.DecimalField(max_digits=30, decimal_places=1, null=True)
    data = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.address