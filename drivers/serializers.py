from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class FindingDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindingDriver
        fields = "__all__"
