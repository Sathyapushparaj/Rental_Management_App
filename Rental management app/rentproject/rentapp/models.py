from django.db import models
from django.contrib.auth.models import User
import datetime
import os


def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)


class House(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    safety = models.TextField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Add_place(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    Home_image1 = models.ImageField(upload_to=getFileName, null=True, blank=True)
    Home_image2 = models.ImageField(upload_to=getFileName, null=True, blank=True)
    Home_image3 = models.ImageField(upload_to=getFileName, null=True, blank=True)
    Home_image4 = models.ImageField(upload_to=getFileName, null=True, blank=True)
    address = models.TextField(max_length=800, null=False, blank=False)
    pin_code=models.IntegerField(null=False, blank=False)
    safety = models.TextField(max_length=600, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="default,1-Hidden")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
