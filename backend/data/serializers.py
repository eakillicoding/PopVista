from rest_framework import serializers
from .models import Country, PopulationData


class PopulationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationData
        fields = ['age', 'male', 'female']


class CountrySerializer(serializers.ModelSerializer):
    population_data = PopulationDataSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['name', 'population_data']