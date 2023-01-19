from django.db import models

from common.models import BaseModel


class Province(BaseModel):
    name = models.CharField(max_length=500)


class District(BaseModel):
    name = models.CharField(max_length=500)
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, related_name="districts")


class Municipality(BaseModel):
    name = models.CharField(max_length=500)
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, related_name="municipalities")
