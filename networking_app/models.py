from typing import Any

from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models import JSONField, URLField


# Create your models here.


class NetworkingUserModel(models.Model):
    name=models.CharField(max_length=255)
    image=CloudinaryField(blank=True, null=True)

    phone=models.CharField(max_length=10,blank=True,null=True)

    linkedin_url=models.URLField(blank=True,null=True)
    other_url=models.URLField(blank=True,null=True)

    notes=models.CharField(max_length=255)
    designation=models.CharField(max_length=50)

    location_name=models.CharField(max_length=100)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    created_at=models.DateTimeField(auto_now_add=True)




