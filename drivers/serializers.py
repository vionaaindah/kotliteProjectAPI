from rest_framework import fields, serializers
from .models import *

class FindingDriverSerializer(serializers.ModelSerializer):
    # class serializer for create finding driver
    class Meta:
        model = FindingDriver
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # class serializer for create order and get order data for get optimize route
    class Meta:
        model = Order
        fields = '__all__'

class DriversListSerializer(serializers.ModelSerializer):
    # class serializer for get order and diver data for detail driver and recommendation list
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    phone = serializers.CharField(source='user.additionals.phone', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'first_name', 'last_name', 'phone', 
                'lat_start', 'long_start', 'place_start', 
                'lat_end', 'long_end', 'place_end', 'status',
                'time', 'total_psg', 'capacity', 'car_type', 'income',
            )

class StatusUpdateSerializer(serializers.ModelSerializer):
    # class serializer that use for change status in order
    class Meta:
        model = Order
        fields = ['status']
    