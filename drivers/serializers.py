from rest_framework import fields, serializers
from .models import *

class FindingDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindingDriver
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class DriversListSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    phone = serializers.CharField(source='user.additionals.phone', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name', 'lat_start', 
                'long_start', 'lat_end', 'long_end', 'status',
                'time', 'total_psg', 'capacity', 'car_type', 'income',
                'place_start', 'place_end', 'user', 'phone', 
            )

class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
    