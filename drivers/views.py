from rest_framework import viewsets
from drivers.serializers import *
from drivers.models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *

# class OrderViewSet(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     queryset =  Order.objects.all()
#     serializer_class = OrderSerializer

# class FindingDriverViewSet(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     queryset =  FindingDriver.objects.all()
#     serializer_class = FindingDriverSerializer

class OrderCreateAPIView(CreateAPIView):
    """
    Create a new Order entry with Finding_Driver entry
    """
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)