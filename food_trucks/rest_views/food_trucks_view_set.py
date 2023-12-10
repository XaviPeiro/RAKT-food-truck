from rest_framework import mixins, serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from food_trucks.models import FoodTruck

from food_trucks.services.get_closer_trucks_by_walking import get_closer_trucks_by_walking

class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = '__all__'


class FooTruckViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = FoodTruck.objects.all()
    serializer_class = FoodTruckSerializer

    @action(detail=False, methods=['get'], url_path='get-nearest')
    def get_nearest_food_trucks(self, request):
        """
            Exempli Gratia
            lat = 37.76008693198698
            long = -122.41880648110114
        """
        lat = request.query_params.get('latitude')
        long = request.query_params.get('longitude')
        """
        Ideally I would call to this function but I ran out of time and
        # I got problems creating a Google Billing Account 🤷
        # get_closer_trucks_by_walking()
        """
        number_of_trucks = 5
        nearest_trucks = FoodTruck.get_closest_trucks(latitude=lat, longitude=long, number_of_trucks=number_of_trucks)
        page = self.paginate_queryset(nearest_trucks)
        serializer = self.get_serializer(page or nearest_trucks, many=True)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
