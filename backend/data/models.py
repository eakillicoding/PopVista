from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PopulationData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='population_data')
    age = models.CharField(max_length=10, unique=True)
    male = models.FloatField()
    female = models.FloatField()

    def __str__(self):
        return f"Age: {self.age}, Male: {self.male}, Female: {self.female}"
