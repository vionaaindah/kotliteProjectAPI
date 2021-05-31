from rest_framework import serializers
from .models import *

class PassengersSerializer(serializers.ModelSerializer):
    # class serializer for create Passengers
    class Meta:
        model = Passengers
        fields = '__all__'

class PassengersListSerializer(serializers.ModelSerializer):
    # class serializer for get passengers detail
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    phone = serializers.CharField(source='user.additionals.phone', read_only=True)
    driver_id = serializers.IntegerField(source='order.user.pk', read_only=True)
    
    class Meta:
        model = Passengers
        fields = ('id', 'user', 'first_name', 'last_name', 'phone', 
                'lat_pick', 'long_pick', 'place_pick', 
                'lat_drop', 'long_drop', 'place_drop','status',
                'time', 'fee', 'distance', 'time_taken', 'order', 'driver_id',
            )

class StatusUpdateSerializer(serializers.ModelSerializer):
    # class serializer for change status passengers
    class Meta:
        model = Passengers
        fields = ['status']
    