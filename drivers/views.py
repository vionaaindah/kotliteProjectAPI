from rest_framework import viewsets
from drivers.serializers import *
from drivers.models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class OrderViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset =  Order.objects.all()
    serializer_class = OrderSerializer

class FindingDriverViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset =  FindingDriver.objects.all()
    serializer_class = FindingDriverSerializer