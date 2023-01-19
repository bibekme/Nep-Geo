from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Province, District, Municipality

from .serializers import ProvinceSerializer, DistrictSerializer, MunicipalitySerializer


class ProvinceViewSet(ReadOnlyModelViewSet):
    lookup_field = "idx"
    serializer_class = ProvinceSerializer
    queryset = Province.objects.filter(is_obsolete=False).all()


class DistrictViewSet(ReadOnlyModelViewSet):
    lookup_field = "idx"
    serializer_class = DistrictSerializer
    queryset = District.objects.filter(is_obsolete=False).all()

    def get_queryset(self):
        query_parm = self.request.query_params.get("province")
        if not query_parm:
            return self.queryset
        else:
            return District.objects.filter(province__idx=query_parm).all()

    @swagger_auto_schema(manual_parameters=[openapi.Parameter("province", openapi.IN_QUERY, description="The province idx you want to districts for", type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request)


class MunicipalityViewSet(ReadOnlyModelViewSet):
    lookup_field = "idx"
    serializer_class = MunicipalitySerializer
    queryset = Municipality.objects.filter(is_obsolete=False).all()

    def get_queryset(self):
        query_parm = self.request.query_params.get("district")
        if not query_parm:
            return self.queryset
        else:
            return Municipality.objects.filter(district__idx=query_parm).all()

    @swagger_auto_schema(manual_parameters=[openapi.Parameter("district", openapi.IN_QUERY, description="The district idx you want to municipalities for", type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request)
