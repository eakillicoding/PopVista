from django.urls import path
from .views import CountryPopulationListView


urlpatterns = [
    path('countries/population/', CountryPopulationListView.as_view(), name='country-population-list'),
]