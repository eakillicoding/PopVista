from rest_framework.generics import ListAPIView
from .models import Country
from .serializers import CountrySerializer


class CountryPopulationListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer