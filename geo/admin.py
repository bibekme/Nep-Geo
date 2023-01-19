from django.contrib import admin

from common.admin import BaseAdmin
from . import models


@admin.register(models.Province)
class ProvinceAdmin(BaseAdmin):
    pass


@admin.register(models.District)
class DistrictAdmin(BaseAdmin):
    def get_list_display(self, request):
        return super().get_list_display(request, 'province')


@admin.register(models.Municipality)
class MunicipalityAdmin(BaseAdmin):
    def get_list_display(self, request):
        return super().get_list_display(request, "district")
