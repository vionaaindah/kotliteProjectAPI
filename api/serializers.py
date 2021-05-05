from rest_framework import serializers
from api.models import order, finding_driver, request, transaction
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = "__all__"

class finding_driverSerializer(serializers.ModelSerializer):
    class Meta:
        model = finding_driver
        fields = "__all__"

class requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = request
        fields = "__all__"

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = "__all__"