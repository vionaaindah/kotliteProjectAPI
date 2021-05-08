from rest_framework import serializers
from .models import *

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = "__all__"

class finding_driverSerializer(serializers.ModelSerializer):
    class Meta:
        model = finding_driver
        fields = "__all__"
