from rest_framework import serializers
from .models import *

class requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = request
        fields = "__all__"

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = "__all__"