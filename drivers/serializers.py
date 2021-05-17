from rest_framework import fields, serializers
from .models import *

class FDSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindingDriver
        exclude = ['order', 'time']

class OrderCreateSerializer(serializers.ModelSerializer):
    findingdriver = FDSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'lat_start', 'long_start', 'lat_end', 'long_end', 'time', 'capacity', 'findingdriver']

    def create(self, validated_data):
        fds_data = validated_data.pop('findingdriver')
        order = Order.objects.create(status ='Finding', total_psg=0, **validated_data)
        for fd_data in fds_data:
            FindingDriver.objects.create(order=order, time=order.time, **fd_data)
        return order

class FindingDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindingDriver
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'