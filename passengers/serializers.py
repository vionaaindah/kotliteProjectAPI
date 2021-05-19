from rest_framework import serializers
from .models import *

class PassengersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = ['order', 'user', 'status', 'lat_pick', 
                    'long_pick', 'lat_drop', 'long_drop', 'time',]

class PassengersListSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    class Meta:
        model = Passengers
        fields = ('id', 'first_name', 'last_name', 'lat_pick', 
                'long_pick', 'lat_drop', 'long_drop', 'status',
                'time', 'fee', 'distance', 'time_taken', 'order',
            )

class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = ['status']
    