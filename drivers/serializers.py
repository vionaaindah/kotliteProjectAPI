from rest_framework import serializers
from .models import *

class OrderCreateSerializer(serializers.ModelSerializer):
    """
    Serializer to Add Order together with FindingDriver
    """

    class FindingDriverTempSerializer(serializers.ModelSerializer):
        class Meta:
            model = FindingDriver
            # 'order' is a FK which will be assigned after creation of 'Order' model entry
            exclude = ['order', 'time']

    finding_driver = FindingDriverTempSerializer()  

    class Meta:
        model = Order
        exclude = ['status', 'total_psg', 'user']

    def create(self, request, validated_data):
        finding_driver_data = validated_data.pop('finding_driver')
        order_instance = Order.objects.create(**validated_data)
        for finding_data in finding_driver_data:
            FindingDriver.objects.create(order=order_instance,
                                  user=request.user,
                                  time=order_instance.time,
                                  **finding_data)
        return order_instance