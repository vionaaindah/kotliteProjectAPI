from rest_framework import serializers
from .models import *

class PassengersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = "__all__"
