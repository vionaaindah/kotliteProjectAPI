from rest_framework import serializers
from .models import *

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"