from rest_framework import serializers

from .models import Province, District, Municipality


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['idx', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['idx', 'name']


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ['idx', 'name']
