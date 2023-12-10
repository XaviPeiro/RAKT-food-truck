from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point



class FoodTruck(models.Model):
    id = models.CharField(max_length=11, primary_key=True)  # Could be interesting to model this data-type
    name = models.CharField(max_length=255)
    food_description = models.TextField()
    address = models.CharField(max_length=255)  # Can be longer?
    latitude_longitude_geo = models.PointField()

    @staticmethod
    def get_closest_trucks(latitude: float, longitude: float, number_of_trucks: int):
        reference_point = Point(float(longitude), float(latitude), srid=4326)
        closest_trucks = FoodTruck.objects.annotate(
            distance=Distance('latitude_longitude_geo', reference_point)
        ).order_by('distance')[:number_of_trucks]

        return closest_trucks
