from rest_framework import fields, serializers
from .models import *

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['status', 'total_psg']

    def create(self, validated_data):
        order = Order.objects.create(status ='Finding', 
                                    total_psg=0, 
                                    **validated_data)
        return order

class FindingDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindingDriver
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'